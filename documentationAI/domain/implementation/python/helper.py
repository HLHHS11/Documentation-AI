# FIXME: プロジェクトルートディレクトリ名とパッケージ名が同じ場合，正しいネームスペースが得られない！！！
import os
import ast
# from importlib import util

from documentationAI.domain.services.analyzer import IAnalyzerHelper
from documentationAI.domain.implementation.python.symbol import PythonSymbolId
from documentationAI.domain.models.symbol import ISymbolId


class PythonAnalyzerHelper(IAnalyzerHelper):

    def __init__(self):
        pass


    def parse_symbol_id_str(self, symbol_id_str: str) -> PythonSymbolId:
        return PythonSymbolId.parse(symbol_id_str)

    def abspath_to_namespace(self, module_abs_path: str, package_root_path: str) -> str:

        if not os.path.isabs(module_abs_path):
            raise ValueError(f"filepath: {module_abs_path} is not absolute path.")
        if not module_abs_path.endswith('.py'):
            raise ValueError(f"filepath: {module_abs_path} is not python file. (not ends with '.py')")

        package_parent_dir = os.path.join(package_root_path, "..")      
        namespace_draft = os.path.relpath(module_abs_path, package_parent_dir)
        namespace_draft = namespace_draft[:-3]
        namespace_draft = namespace_draft.replace(os.sep, '.')
        namespace = namespace_draft

        return namespace

    def namespace_to_abspath(self, namespace: str, package_root_dir: str) -> str:
        # namespaceから，パッケージ名に対応する部分を取り除く。すなわち，"."で区切って最初の要素を取り除いてから，残りを"."で再度結合する
        # 以下に実装
        remove_package_name = ".".join(namespace.split(".")[1:])
        return os.path.join(package_root_dir, remove_package_name.replace('.', os.sep) + '.py')
        # return os.path.join(root_dir, namespace.replace('.', os.sep) + '.py')

    def get_symbol_def(self, symbol_id: ISymbolId, package_root_dir: str) -> str:
        module_path = self.namespace_to_abspath(symbol_id.namespace, package_root_dir)
        with open(module_path, "r") as file:
            tree = ast.parse(file.read())
        # `symbol_id`に対応するソース定義を取得
        for node in ast.walk(tree):
            if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
                if node.name == symbol_id.symbol_name:
                    return ast.unparse(node)
                if node.name == symbol_id.symbol_name.split(".")[-1]:
                    return ast.unparse(node)
            elif isinstance(node, (ast.AnnAssign, ast.AugAssign)):
                # NOTE: pylance警告を無視している
                if node.target.id == symbol_id.symbol_name.split(".")[-1]:  # type: ignore
                    return ast.unparse(node)
            elif isinstance(node, ast.Assign):
                # NOTE: pylance警告を無視している
                if node.targets[0].id == symbol_id.symbol_name.split(".")[-1]:  # type: ignore
                    return ast.unparse(node)
        raise ValueError(f"symbol_id: {symbol_id} is not found in {module_path}")
