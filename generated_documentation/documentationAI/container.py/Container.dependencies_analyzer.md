# `Container.dependencies_analyzer`のソース定義ファイル

```python
dependencies_analyzer = providers.Singleton(PythonDependenciesAnalyzer, package_name=package_name, parser=python_symbol_parser)
```

`Container.dependencies_analyzer`は、`PythonDependenciesAnalyzer`クラスのインスタンスをシングルトンとして提供します。このインスタンスは、`package_name`と`parser`を引数として初期化されます。

# `Container.dependencies_analyzer`が依存関係にあるシンボルのドキュメント

依存する外部シンボルのドキュメントは以下の通りである。ただし、１つも存在しない場合もあり得る。

---

## documentationAI.domain.models.code_analyzer.python_limited.dependencies_analyzer:PythonDependenciesAnalyzer

`PythonDependenciesAnalyzer`は、`IDependenciesAnalyzer`インターフェースを実装したクラスです。このクラスは、Pythonのソースコードの依存関係を解析するための機能を提供します。

### コンストラクタ

#### `__init__(self, package_name: str, parser: Callable[[list[str], str], PythonSymbolInfo | str])`

- `package_name` (str): 解析対象のパッケージ名
- `parser` (Callable[[list[str], str], PythonSymbolInfo | str]): シンボル情報を解析するためのパーサー関数

### メソッド

#### `analyze(self, file_path: str) -> Tuple[str, Dict[str, list[PythonSymbolInfo]]]`

指定されたファイルの依存関係を解析します。

- `file_path` (str): 解析対象のファイルパス
- 戻り値: ネームスペースとシンボルの依存関係を示す辞書

#### `parse_symbol_str(self, symbol_str: str) -> PythonSymbolInfo`

指定されたシンボル情報を解析します。

- `symbol_str` (str): 解析対象のシンボル情報
- 戻り値: 解析結果のシンボル情報

#### `get_symbol_definition(self, file_path: str, symbol_name: str) -> str`

指定されたファイルとシンボル名に対するシンボルの定義を取得します。

- `file_path` (str): 解析対象のファイルパス
- `symbol_name` (str): 解析対象のシンボル名
- 戻り値: シンボルの定義

#### `get_file_contents(self, file_path: str) -> str`

指定されたファイルの内容を取得します。

- `file_path` (str): 解析対象のファイルパス
- 戻り値: ファイルの内容

### 内部メソッド

#### `_collect_imports(self, tree: ast.AST) -> list[ast.Import | ast.ImportFrom]`

指定されたASTツリーからインポート文を収集します。

- `tree` (ast.AST): 解析対象のASTツリー
- 戻り値: 収集されたインポート文のリスト

#### `_get_top_level_symbol_nodes(self, tree: ast.AST) -> list[ast.AST]`

指定されたASTツリーからトップレベルのシンボルノードを取得します。

- `tree` (ast.AST): 解析対象のASTツリー
- 戻り値: トップレベルのシンボルノードのリスト

#### `_analyze_dependencies(self, top_level_symbol_nodes: list[ast.AST], import_nodes: list[ast.Import | ast.ImportFrom]) -> Dict[str, list[PythonSymbolInfo]]`

指定されたトップレベルのシンボルノードとインポートノードからシンボルの依存関係を解析します。

- `top_level_symbol_nodes` (list[ast.AST]): トップレベルのシンボルノードのリスト
- `import_nodes` (list[ast.Import | ast.ImportFrom]): インポートノードのリスト
- 戻り値: シンボルの依存関係を示す辞書

### 依存関係

`PythonDependenciesAnalyzer`は、以下の外部シンボルに依存しています。

- `IDependenciesAnalyzer`: `PythonDependenciesAnalyzer`が実装するインターフェース
- `filepath_to_namespace`: ファイルパスをネームスペースに変換するための関数

---

## documentationAI.domain.models.code_analyzer.python_limited.dependencies_analyzer:python_symbol_parser

`python_symbol_parser`は、`PythonDependenciesAnalyzer`クラスのコンストラクタで使用されるパーサー関数です。

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

`python_symbol_parser`は、`GetSymbolInfo`モードと`GetFilePath`モードの2つのモードで使用されます。`GetSymbolInfo`モードでは、引数の文字列を`PythonSymbolInfo`に変換して返します。`GetFilePath`モードでは、引数の文字列からファイルパスを取得して返します。

---

依存する外部シンボルのドキュメントは以下の通りである。ただし、１つも存在しない場合もあり得る。