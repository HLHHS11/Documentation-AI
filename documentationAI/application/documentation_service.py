from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage
from openai import InvalidRequestError

from documentationAI.utils.topological_sort import topological_sort
from documentationAI.domain.repositories.interfaces import IDocumentRepository
from documentationAI.domain.services.analyzer import IAnalyzerHelper, IPackageAnalyzer
from documentationAI.domain.models.document import Document
from documentationAI.domain.services.prompt_generator.documentation import DocumentationPromptGenerator, DocumentationPromptGeneratorContext


class DocumentationService:

    def __init__(
            self,
            package_analyzer: IPackageAnalyzer,
            document_repository: IDocumentRepository,
            helper: IAnalyzerHelper,
            prompt_generator: DocumentationPromptGenerator
    ):
        self.package_analyzer = package_analyzer
        self.document_repository = document_repository
        self.helper = helper
        self.prompt_generator = prompt_generator

    def generate_package_documentation(
        self,
        project_root_dir: str,
        package_root_dir: str,
        package_name: str
    ) -> None:
        
        # パッケージ解析サービスを利用して，シンボルの依存関係を取得するとともに，解決順序を取得する
        dependencies_map = self.package_analyzer.generate_dag(package_root_dir, package_name)
        resolved = topological_sort(dependencies_map)

        # 解決された順番にしたがってドキュメンテーション生成を行う。
        for symbol_id in resolved:
            # TODO: 解析対象のファイルで「存在しないモジュールをインポートしている」場合，ここでエラーになる。なぜなら，dependencies_mapは存在するモジュールのシンボル情報を解析して保存した辞書だから。
            required_symbol_ids = dependencies_map[symbol_id]
            # 1. シンボルのソース定義を取得
            print(f"Generating document for {symbol_id.stringify()}...")
            symbol_def = self.helper.get_symbol_def(symbol_id, package_root_dir)

            # 2. 依存先シンボルのドキュメントを取得
            required_symbol_docs: list[Document] = []
            for required_symbol_id in required_symbol_ids:
                required_symbol_doc = self.document_repository.get_by_symbol_id(required_symbol_id)
                if required_symbol_doc: # TODO: 見つからなければ何をするのか，具体的に考えておくこと
                    required_symbol_docs.append(required_symbol_doc)
            
            # 3. AIに投げるための質問文を生成
            context = DocumentationPromptGeneratorContext.from_dict({
                "symbol_id": symbol_id,
                "symbol_def": symbol_def,
                "required_symbol_docs": required_symbol_docs,
            })
            prompt = self.prompt_generator.generate(context)

            # 4. AIにプロンプトを投げて，返ってきた返答をドキュメントとして保存
            chat = ChatOpenAI(temperature = 0.25)
            messages = [HumanMessage(content = prompt)]
            try:
                response = chat(messages)
            # TODO: 例外処理をもっと丁寧に書く
            except InvalidRequestError as e:
                print(e)
                print(f"An error occurred and skipped generating documentation for {symbol_id.stringify()}.")
                self.document_repository.save(Document(
                    symbol_id = symbol_id,
                    content = "",
                    succeeded = False
                ))
                continue
 
            response = chat(messages)
            response_text = response.content
            generated_document = Document(  # TODO: よしなに生成する。これ専用にファクトリメソッドを作ってもいい
                symbol_id = symbol_id,
                # dependencies = required_symbol_id_list,   # TODO: 現時点では`required_symbol_id_list`を直接は利用していないので，コメントアウト
                content = response_text,
                succeeded = True
            )
            self.document_repository.save(generated_document)
            
            print(f"Generated document for {symbol_id.stringify()}.")

        return


if __name__ == "__main__":

    def debug():
        import os
        from documentationAI.domain.implementation.python.package_analyzer import PythonPackageAnalyzer
        from documentationAI.domain.implementation.python.module_analyzer import PythonModuleAnalyzer
        from documentationAI.domain.implementation.python.helper import PythonAnalyzerHelper
        from documentationAI.domain.implementation.python.symbol import PythonSymbolId
        from documentationAI.interfaces.repository.document_repository_impl.in_memory import InMemoryDocumentRepositoryImpl


        helper = PythonAnalyzerHelper()
        module_analyzer = PythonModuleAnalyzer(helper)
        package_analyzer = PythonPackageAnalyzer(module_analyzer, helper)
        prompt_generator = DocumentationPromptGenerator()
        class MockDocumentRepository(InMemoryDocumentRepositoryImpl):
            def __init__(self):
                super().__init__()
            def save(self, document: Document) -> None:
                super().save(document)
                print("\n========saved========")
                print(document.get_content())
            def get_by_symbol_id(self, symbol_id: PythonSymbolId) -> Document:  # type: ignore
                return super().get_by_symbol_id(symbol_id)
        
        document_repository = MockDocumentRepository()

        documentation_service = DocumentationService(
            package_analyzer,
            document_repository,
            helper,
            prompt_generator
        )

        project_root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
        package_root_dir = os.path.join(project_root_dir, "documentationAI")
        package_name = "documentationAI"

        documentation_service.generate_package_documentation(project_root_dir, package_root_dir, package_name)

    debug()