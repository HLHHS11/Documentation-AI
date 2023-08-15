# FIXME: プロジェクトルートディレクトリ名とパッケージ名が同じ場合，正しいネームスペースが得られない！！！
import os

from documentationAI.domain.models.package_analyzer.abc import IAnalyzerHelper
from documentationAI.domain.models.package_analyzer.python_limited.symbol_info import PythonSymbolInfo


class PythonAnalyzerHelper(IAnalyzerHelper):

    def __init__(self):
        pass


    def parse_symbol_str(self, symbol_str: str) -> PythonSymbolInfo:
        return PythonSymbolInfo.parse(symbol_str)


    def abspath_to_namespace(self, abspath: str, package_name: str = "") -> str:

        if abspath.endswith('.py'):
            abspath = abspath[:-3]
            namespace = abspath.replace(os.sep, '.')

            # pakcage_nameが指定されていれば，ネームスペースをそのパッケージ名で始まるものに変換する
            if package_name:
                package_name_with_dot = package_name + '.'
                if package_name_with_dot in namespace:
                    namespace = namespace[namespace.index(package_name_with_dot):]
            
            return namespace
        else:
            raise ValueError(f"filepath: {abspath} is not python file. (not ends with '.py')")
    

    def namespace_to_abspath(self, namespace: str, root_dir: str) -> str:
        return os.path.join(root_dir, namespace.replace('.', os.sep) + '.py')
