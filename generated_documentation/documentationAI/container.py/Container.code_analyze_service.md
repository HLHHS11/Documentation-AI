# `Container.code_analyze_service`のソース定義ファイル

```python
code_analyze_service = providers.Singleton(CodeAnalyzeService, code_analyzer=code_analyzer, parser=python_symbol_parser)
```

`Container.code_analyze_service`は、`CodeAnalyzeService`のインスタンスをシングルトンとして提供するプロバイダです。このプロバイダは、`code_analyzer`と`python_symbol_parser`という依存関係を持ちます。

# `Container.code_analyze_service`が依存関係にあるシンボルのドキュメント

依存する外部シンボルのドキュメントは以下の通りです。

## `documentationAI.domain.services.code_analyze_service:CodeAnalyzeService`

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

## `documentationAI.domain.models.code_analyzer.python_limited.dependencies_analyzer:python_symbol_parser`

`python_symbol_parser`は、Pythonのシンボル情報を解析するための関数です。

```python
def python_symbol_parser(args: list[str], mode: str) -> PythonSymbolInfo | str:
    """_summary_
    `GetSymbolInfo`モード: 引数の文字列を`PythonSymbolInfo`に変換して返します。`args[0] = symbol_str = <namespace>:<symbol_name>`の形式  
    `GetFilePath`モード: 引数の文字列からファイルパスを取得して返します。`args[0] = symbol_str = <namespace>:<symbol_name>, args[1] = <root_dir_path>`の形式
    Args:
        args (list[str]): 引数の文字列のリスト
        mode (str): モードを指定する文字列

    Returns:
        PythonSymbolInfo|str: _description_
    """
    if mode == 'GetSymbolInfo':
        symbol_str = args[0]
        return PythonSymbolInfo.parse(symbol_str)
    elif mode == 'GetFilePath':
        symbol_str = args[0]
        root_dir_path = args[1]
        (namespace, _) = symbol_str.split(':')
        return os.path.join(root_dir_path, namespace.replace('.', os.sep) + '.py')
    else:
        raise ValueError(f'Invalid mode: {mode}')
```

`python_symbol_parser`は、`args`と`mode`という2つの引数を受け取り、`PythonSymbolInfo`オブジェクトまたは文字列を返す関数です。`mode`によって処理が分岐し、`GetSymbolInfo`モードでは引数の文字列を`PythonSymbolInfo`に変換して返し、`GetFilePath`モードでは引数の文字列からファイルパスを取得して返します。

この関数は、以下の外部シンボルに依存しています。

- なし