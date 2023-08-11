# `SymbolDocumentationGeneratorService`のソース定義ファイルは以下の通り。

```python
class SymbolDocumentationGeneratorService:

    def __init__(self, code_analyze_service: CodeAnalyzeService, dependencies_analyzer: IDependenciesAnalyzer):
        self.code_analyze_service = code_analyze_service
        self.dependencies_analyzer = dependencies_analyzer
        self.parser = self.code_analyze_service.parser

    def generate(self, root_dir: str, symbol_info_str: str, dependencies: list[str]) -> None:
        file_path = self._get_file_path(symbol_info_str, root_dir)
        symbol_name = self._get_symbol_info(symbol_info_str).symbol_name
        symbol_definition = self.dependencies_analyzer.get_symbol_definition(file_path, symbol_name)
        dependency_docs: Dict[str, str] = {}
        for dependency_symbol_str in dependencies:
            print(f'dependency_symbol_str: {dependency_symbol_str}')
            dependency_path = self._calculate_doc_path(root_dir, dependency_symbol_str)
            dependency_doc = self._read_documentation(dependency_path)
            if dependency_doc:
                dependency_docs[dependency_symbol_str] = dependency_doc
        assembled_doc = self._assemble_documentation(symbol_name, symbol_definition, dependency_docs)
        preamble = f'あなたは優秀なソフトウェアエンジニアです。\n        以下に与えられるPythonのソースコードと周辺情報を読みながらドキュメント生成を行ってください。ただし，ドキュメントのスタイルは，MDN Web DocsのJavaScriptの解説ページのようなスタイルで，**マークダウン形式**で出力してください。\n        '
        prompt = '' + preamble + assembled_doc
        chat = ChatOpenAI(temperature=0.3)
        messages = [SystemMessage(content=preamble), HumanMessage(content=assembled_doc)]
        response = chat(messages)
        response_text = response.content
        print(response_text)
        save_path = self._calculate_doc_path(root_dir, symbol_info_str)
        with open(save_path, 'w') as file:
            file.write(response_text)

    def _get_file_path(self, symbol_info_str: str, root_dir: str) -> str:
        args: list[str] = []
        args.append(symbol_info_str)
        args.append(root_dir)
        mode = 'GetFilePath'
        file_path: str = self.parser(args, mode)
        return file_path

    def _get_symbol_info(self, symbol_info_str: str) -> ISymbolInfo:
        args: list[str] = []
        args.append(symbol_info_str)
        mode = 'GetSymbolInfo'
        symbol_info: ISymbolInfo = self.parser(args, mode)
        return symbol_info

    def _calculate_doc_path(self, root_dir: str, symbol_str: str) -> str:
        file_path = self._get_file_path(symbol_str, root_dir)
        relative_path = os.path.relpath(file_path, root_dir)
        symbol_name = self._get_symbol_info(symbol_str).symbol_name
        doc_path = os.path.join(root_dir, 'generated_documentation/', relative_path, f'{symbol_name}.md')
        return doc_path

    def _read_documentation(self, path: str) -> str:
        try:
            with open(path, 'r') as file:
                return file.read()
        except FileNotFoundError:
            print(f'Warning: Documentation not found for {path}')
            return ''

    def _assemble_documentation(self, symbol_name: str, symbol_definition: str, dependency_docs: Dict[str, str]) -> str:
        assembled_doc = f'\n# `{symbol_name}`のソース定義ファイルは以下の通り。\n<pythonscript id="{symbol_name}>\n{symbol_definition}\n</pythonscript>\n# `{symbol_name}`が依存関係にあるシンボルのドキュメント\n依存する外部シンボルのドキュメントは以下の通りである。ただし，１つも存在しない場合もあり得る。\n'
        for (dependency_symbol_str, dependency_doc) in dependency_docs.items():
            to_be_appended = f'---\n## {dependency_symbol_str}\n<dependencydoc id="{dependency_symbol_str}">\n{dependency_doc}\n</dependencydoc>\n---\n\n'
            assembled_doc += to_be_appended
        return assembled_doc
```

# `SymbolDocumentationGeneratorService`が依存関係にあるシンボルのドキュメント
依存する外部シンボルのドキュメントは以下の通りである。ただし，１つも存在しない場合もあり得る。

---

## documentationAI.domain.models.code_analyzer.abc:ISymbolInfo
<dependencydoc id="documentationAI.domain.models.code_analyzer.abc:ISymbolInfo">

## `ISymbolInfo`クラス

`ISymbolInfo`クラスは、抽象基底クラス（`abc.ABC`）であり、シンボル情報を表すためのインターフェースです。

### プロパティ

- `namespace`（str）: シンボルの名前空間を表す文字列です。
- `symbol_name`（str）: シンボルの名前を表す文字列です。

### メソッド

- `stringify() -> str`: シンボル情報を文字列に変換します。このメソッドはサブクラスで実装する必要があります。
- `parse(stringified: str) -> ISymbolInfo`: 文字列からシンボル情報を復元します。このメソッドはクラスメソッドとして実装する必要があります。

### サブクラス

`ISymbolInfo`クラスは抽象基底クラスであるため、具象クラスを作成する必要があります。

### 依存する外部シンボルのドキュメント

`ISymbolInfo`クラスは、依存する外部シンボルのドキュメントが存在する場合、それらのドキュメントを参照する必要があります。ただし、依存する外部シンボルのドキュメントが存在しない場合もあります。

</dependencydoc>

---

---

## documentationAI.domain.services.code_analyze_service:CodeAnalyzeService
<dependencydoc id="documentationAI.domain.services.code_analyze_service:CodeAnalyzeService">

# CodeAnalyzeService

`CodeAnalyzeService`は、コード解析に関するサービスを提供するクラスです。

## コンストラクタ

### `__init__(self, code_analyzer: ICodeAnalyzer, parser: Callable[[list[str], str], ISymbolInfo | str]) -> None`

`CodeAnalyzeService`のインスタンスを初期化します。

- `code_analyzer`（`ICodeAnalyzer`）: コード解析を行うためのインターフェースを実装したオブジェクトです。
- `parser`（`Callable[[list[str], str], ISymbolInfo | str]`）: シンボル情報を解析するための関数です。

## メソッド

### `resolve_dependencies(self, package_root_dir: str) -> DependenciesNamedTuple`

指定されたパッケージの依存関係を解決します。

- `package_root_dir`