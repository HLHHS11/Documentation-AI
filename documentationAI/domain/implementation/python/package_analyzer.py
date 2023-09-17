from typing import Dict
import os

from documentationAI.domain.services.analyzer import IAnalyzerHelper, IPackageAnalyzer
from documentationAI.domain.implementation.python.symbol import PythonSymbolId
from documentationAI.domain.implementation.python.module_analyzer import PythonModuleAnalyzer


class PythonPackageAnalyzer(IPackageAnalyzer):

    def __init__(
        self,
        module_analyzer: PythonModuleAnalyzer,
        helper: IAnalyzerHelper
    ):
        self.module_analyzer = module_analyzer
        self.helper = helper
    

    # PythonDependenciesAnalyzerを使って，root_dir以下のファイルを解析し，依存関係を取得
    def generate_dag(    # type: ignore `ISymbolId`と`PythonSymbolId`の互換性に関する警告を無視
        self,
        package_root_dir: str,
        package_name: str
    ) -> Dict[PythonSymbolId, list[PythonSymbolId]]:

        overall_dependencies: Dict[str, Dict[str, list[PythonSymbolId]]] = {}
        # ルートディレクトリ以下の全pythonソースに対して処理を行う
        for dirpath, _, filenames in os.walk(package_root_dir):
            for filename in filenames:
                if filename.endswith('.py'):
                    module_path = os.path.join(dirpath, filename)
                    namespace, symbols_dependencies = self.module_analyzer.analyze(module_path, package_root_dir, package_name)
                    # NOTE: `ISymbolInfo`と`PythonSymbolInfo`の問題で，`type: ignore`している。
                    overall_dependencies[namespace] = symbols_dependencies  # type: ignore
        
        # 依存関係をDAGに変換
        # dag: Dict[str, list[str]] = {}
        dag: Dict[PythonSymbolId, list[PythonSymbolId]] = {}
        for namespace, dependencies in overall_dependencies.items():
            for symbol_name, required_symbol_ids in dependencies.items():
                # symbol_info_str = PythonSymbolId(namespace, symbol_name).stringify()
                symbol_id = PythonSymbolId(namespace, symbol_name)
                dag[symbol_id] = []
                for required_symbol_id in required_symbol_ids:
                    # 依存先の情報の中に，symbol_name == '*'のものがある場合，当該ファイル内のすべてのトップレベルシンボルをインポートすることを意味する
                    if required_symbol_id.symbol_name == '*':
                        for each_symbol_name in overall_dependencies[required_symbol_id.namespace].keys():
                            dag[symbol_id].append(PythonSymbolId(required_symbol_id.namespace, each_symbol_name))
                    else:
                        dag[symbol_id].append(required_symbol_id)
                    
        return dag
