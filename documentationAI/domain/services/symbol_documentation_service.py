import os
import random
from typing import Dict

from langchain import PromptTemplate
from langchain.llms import OpenAI
# from langchain.models import Completion
# from langchain.chat_models import ChatOpenAI
from langchain.chat_models import ChatOpenAI
from langchain.schema import (
    AIMessage,
    HumanMessage,
    SystemMessage,
)


from documentationAI.domain.models.package_analyzer.abc import IAnalyzerHelper, ISymbolInfo
from documentationAI.domain.services.package_analyze_service import PackageAnalyzeService
from documentationAI.domain.models.package_analyzer.abc import IModuleAnalyzer
# python_symbol_parserにエディタで飛ぶ用のインポート
# from documentationAI.domain.models.package_analyzer.python_limited.module_analyzer import python_symbol_parser



from dotenv import load_dotenv
from documentationAI.settings import dotenv_path

load_dotenv(verbose=True)
load_dotenv(dotenv_path)

OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")

class SymbolDocumentationService:
    
    def __init__(
            self,
            package_analyze_service: PackageAnalyzeService,
            module_analyzer: IModuleAnalyzer,
            helper: IAnalyzerHelper,
            # documentation_generator: DocumentationGenerator,
            # documentation_repository: DocumentationRepository
    ):
        self.package_analyze_service = package_analyze_service
        self.module_analyzer = module_analyzer
        self.helper = helper
        # self.documentation_generator = documentation_generator
        # self.documentation_repository = documentation_repository
    

# NOTE: パッケージ名は，symbol_info_strに含まれているので，引数は`package_root_dir`より`root_dir`が適切
    def generate(
        self,
        root_dir: str,
        symbol_info_str: str,
        dependencies: list[str]
    ) -> None:

        # file_path = self._get_file_path(symbol_info_str, root_dir)
        symbol_info = self.helper.parse_symbol_str(symbol_info_str)
        symbol_name = symbol_info.symbol_name
        namespace = symbol_info.namespace
        file_path = self.helper.namespace_to_abspath(namespace, root_dir)

        # シンボルのソース定義を取得
        symbol_definition = self.module_analyzer.get_symbol_impl(file_path, symbol_name)

        # 依存関係にあるシンボルのドキュメントを取得
        dependency_docs: Dict[str, str] = {}
        for dependency_symbol_str in dependencies:
            # NOTE: `dependency_symbol_str`がどのようなものか確認
            print(f"dependency_symbol_str: {dependency_symbol_str}")
            dependency_path = self._calculate_doc_path(root_dir, dependency_symbol_str)
            dependency_doc = self._read_documentation(dependency_path)
            if dependency_doc:
                dependency_docs[dependency_symbol_str] = dependency_doc

        assembled_doc = self._assemble_documentation(symbol_name, symbol_definition, dependency_docs)


        # AIに投げるプロンプトを生成
        preamble = f"""あなたは優秀なソフトウェアエンジニアです。
        以下に与えられるPythonのソースコードと周辺情報を読みながらドキュメント生成を行ってください。ただし，ドキュメントのスタイルは，MDN Web DocsのJavaScriptの解説ページのようなスタイルで，**マークダウン形式**で出力してください。
        """
        prompt = "" + preamble + assembled_doc
        
        chat = ChatOpenAI(temperature=0.3)

        messages = [
            SystemMessage(content=preamble),
            HumanMessage(content=assembled_doc)
        ]
        response = chat(messages)
        response_text = response.content
        print(response_text)

        # AIに投げる
        # AIに投げる処理のモック
        # response_text = f"AIからの返答です。乱数: {random.randint(0, 1000)}"
        # 返答の保存先
        save_path = self._calculate_doc_path(root_dir, symbol_info_str)
        with open(save_path, 'w') as file:
            file.write(response_text)



    # def _get_file_path(self, symbol_info_str: str, root_dir: str) -> str:
    #     args: list[str] = []
    #     args.append(symbol_info_str)
    #     args.append(root_dir)
    #     mode = "GetFilePath"
    #     file_path: str = self.parser(args, mode) # type: ignore
    #     return file_path
    
    # def _get_symbol_info(self, symbol_info_str: str) -> ISymbolInfo:
    #     args: list[str] = []
    #     args.append(symbol_info_str)
    #     mode = "GetSymbolInfo"
    #     symbol_info: ISymbolInfo = self.parser(args, mode) # type: ignore
    #     return symbol_info


    # NOTE: generated by ChatGPT
    def _calculate_doc_path(self, root_dir: str, symbol_str: str) -> str:
        # 依存先シンボルの情報からファイルパスを取得
        # file_path = self._get_file_path(symbol_str, root_dir)
        symbol_info = self.helper.parse_symbol_str(symbol_str)
        symbol_name = symbol_info.symbol_name
        namespace = symbol_info.namespace
        file_path = self.helper.namespace_to_abspath(namespace, root_dir)
        # root_dirからの相対パスを取得
        relative_path = os.path.relpath(file_path, root_dir)
        # ドキュメントの保存先パスを計算
        # symbol_name = self._get_symbol_info(symbol_str).symbol_name
        doc_path = os.path.join(root_dir, "generated_documentation/", relative_path, f"{symbol_name}.md")
        return doc_path

    def _read_documentation(self, path: str) -> str:
        try:
            with open(path, 'r') as file:
                return file.read()
        except FileNotFoundError:
            print(f"Warning: Documentation not found for {path}")
            # return None
            return ""
    
    def _assemble_documentation(self, symbol_name: str, symbol_definition: str, dependency_docs: Dict[str, str]) -> str:
    # シンボルのソース定義と依存関係にあるシンボルのドキュメントを組み合わせる

        assembled_doc = f"""
# `{symbol_name}`のソース定義ファイルは以下の通り。
<pythonscript id="{symbol_name}>
{symbol_definition}
</pythonscript>
# `{symbol_name}`が依存関係にあるシンボルのドキュメント
依存する外部シンボルのドキュメントは以下の通りである。ただし，１つも存在しない場合もあり得る。
"""
        for dependency_symbol_str, dependency_doc in dependency_docs.items():
            to_be_appended = f"""---
## {dependency_symbol_str}
<dependencydoc id="{dependency_symbol_str}">
{dependency_doc}
</dependencydoc>
---

"""
            assembled_doc += to_be_appended

        return assembled_doc

