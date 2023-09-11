from typing import Dict
import os

from documentationAI.domain.services.package_analyzer.abc import IAnalyzerHelper, IPackageAnalyzer
from documentationAI.domain.services.package_analyzer.python.symbol_info import PythonSymbolInfo
from documentationAI.domain.services.package_analyzer.python.module_analyzer import PythonModuleAnalyzer


class PythonPackageAnalyzer(IPackageAnalyzer):

    def __init__(
        self,
        module_analyzer: PythonModuleAnalyzer,
        helper: IAnalyzerHelper
    ):
        # super().__init__(module_analyzer, helper)
        self.module_analyzer = module_analyzer
        self.helper = helper
    

    # PythonDependenciesAnalyzerを使って，root_dir以下のファイルを解析し，依存関係を取得
    def generate_dag(
        self,
        package_root_dir: str,
        package_name: str
    ) -> Dict[str, list[str]]:

        # NOTE: pylanceの型チェック`ISymbolInfo`と`PythonSymbolInfo`の問題で，`ISymbolInfo`を選択した
        overall_dependencies: Dict[str, Dict[str, list[PythonSymbolInfo]]] = {}
        # ルートディレクトリ以下の全pythonソースに対して処理を行う
        for dirpath, _, filenames in os.walk(package_root_dir):
            for filename in filenames:
                if filename.endswith('.py'):
                    module_path = os.path.join(dirpath, filename)
                    namespace, symbols_dependencies = self.module_analyzer.analyze(module_path, package_root_dir, package_name)
                    # NOTE: `ISymbolInfo`と`PythonSymbolInfo`の問題で，`type: ignore`している。
                    overall_dependencies[namespace] = symbols_dependencies  # type: ignore
        
        # 依存関係をDAGに変換
        dag: Dict[str, list[str]] = {}
        for namespace, dependencies in overall_dependencies.items():
            for symbol_name, dependent_symbol_infos in dependencies.items():
                symbol_info_str = PythonSymbolInfo(namespace, symbol_name).stringify()
                dag[symbol_info_str] = []
                for dependent_symbol_info in dependent_symbol_infos:
                    # 依存先の情報の中に，symbol_name == '*'のものがある場合，当該ファイル内のすべてのトップレベルシンボルをインポートすることを意味する
                    if dependent_symbol_info.symbol_name == '*':
                        for each_symbol_name in overall_dependencies[dependent_symbol_info.namespace].keys():
                            dag[symbol_info_str].append(PythonSymbolInfo(dependent_symbol_info.namespace, each_symbol_name).stringify())
                    else:
                        dag[symbol_info_str].append(dependent_symbol_info.stringify())
                    
        return dag





