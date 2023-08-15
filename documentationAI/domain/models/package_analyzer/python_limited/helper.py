# FIXME: プロジェクトルートディレクトリ名とパッケージ名が同じ場合，正しいネームスペースが得られない！！！
import os
# from importlib import util

from documentationAI.domain.models.package_analyzer.abc import IAnalyzerHelper
from documentationAI.domain.models.package_analyzer.python_limited.symbol_info import PythonSymbolInfo


class PythonAnalyzerHelper(IAnalyzerHelper):

    def __init__(self):
        pass


    def parse_symbol_str(self, symbol_str: str) -> PythonSymbolInfo:
        return PythonSymbolInfo.parse(symbol_str)


    def abspath_to_namespace(self, abs_path: str, root_dir: str) -> str:

        if not os.path.isabs(abs_path):
            raise ValueError(f"filepath: {abs_path} is not absolute path.")
        if not abs_path.endswith('.py'):
            raise ValueError(f"filepath: {abs_path} is not python file. (not ends with '.py')")

        namespace_draft = os.path.relpath(abs_path, root_dir)
        namespace_draft = namespace_draft[:-3]
        namespace_draft = namespace_draft.replace(os.sep, '.')
        namespace = namespace_draft

        return namespace



    def namespace_to_abspath(self, namespace: str, root_dir: str) -> str:
        return os.path.join(root_dir, namespace.replace('.', os.sep) + '.py')
