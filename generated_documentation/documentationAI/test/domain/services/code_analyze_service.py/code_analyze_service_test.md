# `code_analyze_service_test`のソース定義ファイル

```python
def code_analyze_service_test():
    container.package_name.override('documentationAI')
    service: CodeAnalyzeService = container.code_analyze_service()
    package_root_dir = '/home/yama/Documents/Programming/documentation-AI/documentationAI'
    return service.resolve_dependencies(package_root_dir)
```

# `code_analyze_service_test`が依存関係にあるシンボルのドキュメント

依存する外部シンボルのドキュメントは以下の通りである。ただし、１つも存在しない場合もあり得る。

---

## documentationAI.domain.services.code_analyze_service:CodeAnalyzeService

`CodeAnalyzeService`は、コード解析に関するサービスを提供するクラスです。

### コンストラクタ

#### `__init__(self, code_analyzer: ICodeAnalyzer, parser: Callable[[list[str], str], ISymbolInfo | str]) -> None`

`CodeAnalyzeService`のインスタンスを初期化します。

- `code_analyzer`（`ICodeAnalyzer`）: コード解析を行うためのインターフェースを実装したオブジェクトです。
- `parser`（`Callable[[list[str], str], ISymbolInfo | str]`）: シンボル情報を解析するための関数です。

### メソッド

#### `resolve_dependencies(self, package_root_dir: str) -> DependenciesNamedTuple`

指定されたパッケージの依存関係を解決します。

- `package_root_dir`（`str`）: パッケージのルートディレクトリのパスです。

戻り値は、依存関係を表す`DependenciesNamedTuple`オブジェクトです。

#### `parse_symbol_str(self, symbol_str: str)`

指定されたシンボル文字列を解析します。

- `symbol_str`（`str`）: 解析するシンボル文字列です。

戻り値は解析結果の`ISymbolInfo`オブジェクトです。

## 依存する外部シンボルのドキュメント

`CodeAnalyzeService`は以下の外部シンボルに依存しています。

- [`ICodeAnalyzer`](#documentationAI.domain.models.code_analyzer.abc:ICodeAnalyzer)
- [`topological_sort`](#documentationAI.utils.topological_sort:topological_sort)
- [`ISymbolInfo`](#documentationAI.domain.models.code_analyzer.abc:ISymbolInfo)

---

## documentationAI.container:container

### `container`のソース定義ファイル

```python
container = Container()
```

### `container`が依存関係にあるシンボルのドキュメント

依存する外部シンボルのドキュメントは以下の通りである。ただし、１つも存在しない場合もあり得る。

---