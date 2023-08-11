# `SymbolDocumentationGeneratorService.__init__`

## ソース定義

```python
def __init__(self, code_analyze_service: CodeAnalyzeService, dependencies_analyzer: IDependenciesAnalyzer):
    self.code_analyze_service = code_analyze_service
    self.dependencies_analyzer = dependencies_analyzer
    self.parser = self.code_analyze_service.parser
```

`SymbolDocumentationGeneratorService`クラスのコンストラクタです。`code_analyze_service`と`dependencies_analyzer`という2つの引数を受け取ります。また、`parser`というインスタンス変数を初期化します。

## 依存する外部シンボルのドキュメント

`SymbolDocumentationGeneratorService.__init__`は以下の外部シンボルに依存しています。

- [`CodeAnalyzeService`](#documentationAI.domain.services.code_analyze_service:CodeAnalyzeService)
- [`IDependenciesAnalyzer`](#documentationAI.domain.models.code_analyzer.abc:IDependenciesAnalyzer)

---

# `CodeAnalyzeService`

`CodeAnalyzeService`は、コード解析に関するサービスを提供するクラスです。

## コンストラクタ

### `__init__(self, code_analyzer: ICodeAnalyzer, parser: Callable[[list[str], str], ISymbolInfo | str]) -> None`

`CodeAnalyzeService`のインスタンスを初期化します。

- `code_analyzer`（`ICodeAnalyzer`）: コード解析を行うためのインターフェースを実装したオブジェクトです。
- `parser`（`Callable[[list[str], str], ISymbolInfo | str]`）: シンボル情報を解析するための関数です。

## メソッド

### `resolve_dependencies(self, package_root_dir: str) -> DependenciesNamedTuple`

指定されたパッケージの依存関係を解決します。

- `package_root_dir`（`str`）: パッケージのルートディレクトリのパスです。

戻り値は、依存関係を表す`DependenciesNamedTuple`オブジェクトです。

### `parse_symbol_str(self, symbol_str: str)`

指定されたシンボル文字列を解析します。

- `symbol_str`（`str`）: 解析するシンボル文字列です。

戻り値は解析結果の`ISymbolInfo`オブジェクトです。

## 依存する外部シンボルのドキュメント

`CodeAnalyzeService`は以下の外部シンボルに依存しています。

- [`ICodeAnalyzer`](#documentationAI.domain.models.code_analyzer.abc:ICodeAnalyzer)
- [`topological_sort`](#documentationAI.utils.topological_sort:topological_sort)
- [`ISymbolInfo`](#documentationAI.domain.models.code_analyzer.abc:ISymbolInfo)

---

# `IDependenciesAnalyzer`

## ソース定義

```python
class IDependenciesAnalyzer(abc.ABC):

    @abc.abstractmethod
    def analyze(self, file_path: str) -> Tuple[str, Dict[str, list[ISymbolInfo]]]:
        pass

    @abc.abstractmethod
    def parse_symbol_str(self, symbol_str: str) -> ISymbolInfo:
        pass

    @abc.abstractmethod
    def get_symbol_definition(self, file_path: str, symbol_name: str) -> str:
        pass

    @abc.abstractmethod
    def get_file_contents(self, file_path: str) -> str:
        pass
```

`IDependenciesAnalyzer`は、依存関係解析に関する抽象クラスです。

## メソッド

### `analyze(self, file_path: str) -> Tuple[str, Dict[str, list[ISymbolInfo]]]`

指定されたファイルの依存関係を解析します。

- `file_path`（`str`）: 解析するファイルのパスです。

戻り値は、解析結果を表すタプルです。タプルの第1要素はファイルの内容を表す文字列であり、第2要素は依存関係を表す辞書です。辞書のキーは依存関係の種類を表し、値は依存するシンボルのリストです。

### `parse_symbol_str(self, symbol_str: str) -> ISymbolInfo`

指定されたシンボル文字列を解析します。

- `symbol_str`（`str`）: 解析するシンボル文字列です。

戻り値は解析結果の`ISymbolInfo`オブジェクトです。

### `get_symbol_definition(self, file_path: str, symbol_name: str) -> str`

指定されたファイルとシンボル名から、シンボルの定義を取得します。

- `file_path`（`str`）: シンボルが定義されているファイルのパスです。
- `symbol_name`（`str`）: 取得するシンボルの名前です。

戻り値はシンボルの定義を表す文字列です。

### `get_file_contents(self, file_path: str) -> str`

指定されたファイルの内容を取得します。

- `file_path`（`str`）: 内容を取得するファイルのパスです。

戻り値はファイルの内容を表す文字列です。

## 依存する外部シンボルのドキュメント

`IDependenciesAnalyzer`は以下の外部シンボルに依存しています。

（依存する外部シンボルのドキュメントはありません）