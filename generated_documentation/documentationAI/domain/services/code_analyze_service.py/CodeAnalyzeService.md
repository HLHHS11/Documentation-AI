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