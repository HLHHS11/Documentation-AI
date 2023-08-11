import ast
from typing import Dict, Tuple, Callable

from documentationAI.domain.models.code_analyzer.abc import ISymbolInfo, IDependenciesAnalyzer
from documentationAI.domain.models.code_analyzer.python_limited.utils import filepath_to_namespace


class PythonSymbolInfo(ISymbolInfo):

    def __init__(self, namespace: str, symbol_name: str):
        self.namespace: str = namespace
        self.symbol_name: str = symbol_name
    
    # ネームスペースとシンボル名を":"で結合した文字列を返す
    def stringify(self) -> str:
        return f"{self.namespace}:{self.symbol_name}"
    
    @classmethod
    def parse(cls, stringified: str) -> 'PythonSymbolInfo':
        namespace, symbol_name = stringified.split(':')
        return cls(namespace, symbol_name)

    def __eq__(self, other: object) -> bool:
        if isinstance(other, PythonSymbolInfo):
            return self.namespace == other.namespace and self.symbol_name == other.symbol_name
        else:
            return False
    
    def __str__(self) -> str:
        return f"PythonSymbolInfo(namespace={self.namespace}, symbol_name={self.symbol_name})"


def parse_python_symbol_str(symbol_str: str) -> PythonSymbolInfo:
    return PythonSymbolInfo.parse(symbol_str)


class PythonDependenciesAnalyzer(IDependenciesAnalyzer):

    def __init__(self, package_name: str, parser: Callable[[str], PythonSymbolInfo]):
        self.package_name: str = package_name
        self.parser: Callable[[str], PythonSymbolInfo] = parser    


    # NOTE: Pylanceは`PythonSymbolInfo`と書いたらダメで`ISymbolInfo`と言ってくるので，`type: ignore`している。
    def analyze(self, file_path: str) -> Tuple[str, Dict[str, list[PythonSymbolInfo]]]:   # type: ignore
        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())
        
        # 対象ファイル内のインポート文を解析する
        import_nodes = self._collect_imports(tree)

        # TODO: 機能拡張の必要性あり。今回は妥協して特定パッケージに関するものだけを抜き出している。相対パスインポートにすら対応していない。
        # 解析したインポート文のうち，self.package_name のパッケージに関するもののみ抜き出す
        target_import_nodes: list[ast.Import|ast.ImportFrom] = []
        for node in import_nodes:
            if isinstance(node, ast.Import):
                for alias in node.names:
                    if alias.name.startswith(self.package_name):
                        target_import_nodes.append(node)
                        break
            # elif isinstance(node, ast.ImportFrom):    # ast.Import|ast.ImportFromに対してast.Importではないので，確実にast.ImportFrom
            else:
                if node.module.startswith(self.package_name) if node.module else False:
                    target_import_nodes.append(node)

        # 解析中のファイル内の，外部からインポートされうるシンボルを解析し，名前を取得
        top_level_symbol_nodes = self._get_top_level_symbol_nodes(tree)

        # 上述の各シンボルが依存している，インポートしてきたシンボルを解析し，依存しているシンボルのDependencyのリストを作成する。
        # すなわち，「importまたはfrom import文でインポートしてきたシンボル」が，各top_level_symbolに依存されているかどうか調べる
        symbols_dependencies = self._analyze_dependencies(top_level_symbol_nodes, target_import_nodes)

        # 扱ったファイルのネームスペースと，symbols_dependenciesをタプルで返す
        # 扱ったファイルのパスを，self.package_name起点のネームスペースに変換 (self.package)
        namespace = filepath_to_namespace(file_path, self.package_name)

        return (namespace, symbols_dependencies)


    # HACK: 強引に`PythonSymbolInfo`クラスを参照しており，危険。一時的な対応である。
    #       いずれは，たとえばDIコンテナによって，うまくパーサーも注入されるようにできると良い。
    def parse_symbol_str(self, symbol_str: str) -> PythonSymbolInfo:
        return self.parser(symbol_str)
    

    # HACK: 本来はこのクラスの責務ではないかも？？
    # TODO: クラスおよびメソッド・メンバ変数の扱い方を検討する必要がある。
    def get_symbol_definition(self, file_path: str, symbol_name: str) -> str:
        with open(file_path, 'r') as file:
            tree = ast.parse(file.read())
        # シンボルネームに対応するソース定義を取得。ただし，関数定義やクラス定義の場合は，関数定義やクラス定義の行全体を取得する。
        # クラス定義の場合は，symbol_nameが<クラス名>.<メソッド・メンバ名>の形式になっていることに注意
        # class_def_nodes: set[ast.ClassDef] = set()
        for node in ast.walk(tree):
            if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
                # if isinstance(node, ast.ClassDef):
                #     class_def_nodes.add(node)
                if node.name == symbol_name.split('.')[-1]:
                    return ast.unparse(node)
            elif isinstance(node, (ast.AnnAssign, ast.AugAssign)):
                if node.target.id == symbol_name.split('.')[-1]:    # TODO: pylance警告が出ている
                    return ast.unparse(node)
            elif isinstance(node, ast.Assign):
                if node.targets[0].id == symbol_name.split('.')[-1]:    # TODO: pylance警告が出ている
                    return ast.unparse(node)
        
        return ""




    def _collect_imports(self, tree: ast.AST) -> list[ast.Import|ast.ImportFrom]:
        import_statements: list[ast.Import|ast.ImportFrom] = []
        for node in ast.walk(tree):
            if isinstance(node, (ast.Import|ast.ImportFrom)):
                import_statements.append(node)
        return import_statements

    
    # TODO: 以下のコードは自動生成なので，正確性は検証が必要
    def _get_top_level_symbol_nodes(self, tree: ast.AST) -> list[ast.AST]:
        top_level_symbol_nodes: list[ast.AST] = []

        function_def_nodes: set[ast.FunctionDef|ast.AsyncFunctionDef] = set()
        for node in ast.walk(tree):
            if isinstance(node, (
                ast.FunctionDef, ast.ClassDef, ast.AsyncFunctionDef,
                ast.AnnAssign, ast.AugAssign,
                ast.Assign,
                # ast.Import, ast.ImportFrom    # NOTE: import文まで入れてしまうと，不用意に扱うべきシンボルが増えてしまうので除外
            )):
                
                for function_def_node in function_def_nodes:
                    if node in ast.walk(function_def_node): # 関数（もしくはメソッド）定義内に存在する文は，トップレベルではないとみなして除外
                        break
                else:
                    if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
                        function_def_nodes.add(node)
                    top_level_symbol_nodes.append(node)
                    continue
            
        return top_level_symbol_nodes


    def _analyze_dependencies(self, top_level_symbol_nodes: list[ast.AST], import_nodes: list[ast.Import|ast.ImportFrom]) -> Dict[str, list[PythonSymbolInfo]]:

        symbols_dependencies: Dict[str, list[PythonSymbolInfo]] = {}

        import_symbols: list[Tuple[str, str, bool]] = []    # (namespace, symbol_name, is_import)

        for node in import_nodes:
            if isinstance(node, ast.Import):
                for alias in node.names:
                    # 以下の第２引数を，import asの場合にはそのエイリアスを入れてあげるようにしたい
                    import_symbols.append((alias.name, alias.asname or alias.name, True))
            else:   # ast.ImportFrom
                for alias in node.names:
                    # TODO: 今はtype-ignoreしてあるが，安全性を今一度検証しておく必要がある。
                    import_symbols.append((node.module, alias.name, False))    # type: ignore

        class_def_nodes: set[ast.ClassDef] = set()
        for node in top_level_symbol_nodes:
            if isinstance(node, ast.ClassDef):
                # クラス定義の場合
                symbol_name = node.name
                class_def_nodes.add(node)
                
            elif isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
                # 関数定義、非同期関数定義の場合
                # クラスのメソッドである場合 = class_def_nodesに含まれている場合
                symbol_name = node.name
                for class_def_node in class_def_nodes:
                    # XXX: ここで，nodeがclass_def_nodeの子孫であるかどうかを判定したいのだが，之であっているのか？？？
                    if node in ast.walk(class_def_node):
                        symbol_name = f"{class_def_node.name}.{node.name}"
                        break
            elif isinstance(node, (ast.AnnAssign, ast.AugAssign)):
                # アノテーション付き代入、拡張代入の場合
                symbol_name = node.target.id if isinstance(node.target, ast.Name) else None
                # クラス変数の場合 = class_def_nodesに含まれている場合
                for class_def_node in class_def_nodes:
                    if node in ast.walk(class_def_node):
                        symbol_name = f"{class_def_node.name}.{symbol_name}"
                        break
            elif isinstance(node, ast.Assign):
                # 代入の場合
                symbol_name = node.targets[0].id if isinstance(node.targets[0], ast.Name) else None
                # クラス変数の場合 = class_def_nodesに含まれている場合
                for class_def_node in class_def_nodes:
                    if node in ast.walk(class_def_node):
                        symbol_name = f"{class_def_node.name}.{symbol_name}"
                        break
            else:
                symbol_name = None

            if symbol_name:
                symbol_infos: list[PythonSymbolInfo] = []
                for child in ast.walk(node):
                    if isinstance(child, ast.Name):
                        for namespace, import_symbol, is_import in import_symbols:
                            if child.id == import_symbol:
                                dependency = PythonSymbolInfo(namespace, import_symbol if not is_import else "*")
                                # HACK: 同一の名前は重複させないようにしたい。
                                if dependency not in symbol_infos:  # inは==による比較と等価であるらしい。そして，値オブジェクトとしての比較には__eq__()が使える。
                                    symbol_infos.append(dependency)
                symbols_dependencies[symbol_name] = symbol_infos

        return symbols_dependencies
