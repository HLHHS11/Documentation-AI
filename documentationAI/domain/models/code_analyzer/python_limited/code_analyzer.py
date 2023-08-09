from typing import Dict
import os

from documentationAI.domain.models.code_analyzer.abc import ICodeAnalyzer
from documentationAI.domain.models.code_analyzer.python_limited.dependencies_analyzer import PythonDependenciesAnalyzer, PythonSymbolInfo


class PythonCodeAnalyzer(ICodeAnalyzer):

    def __init__(
            self,
            dependencies_analyzer: PythonDependenciesAnalyzer,
    ):
        super().__init__(dependencies_analyzer)
    

    # PythonDependenciesAnalyzerを使って，root_dir以下のファイルを解析し，依存関係を取得
    def generate_dag(self, package_root_dir: str) -> Dict[str, list[str]]:

        # NOTE: pylanceの型チェック`ISymbolInfo`と`PythonSymbolInfo`の問題で，`ISymbolInfo`を選択した
        overall_dependencies: Dict[str, Dict[str, list[PythonSymbolInfo]]] = {}
        # ルートディレクトリ以下の全pythonソースに対して処理を行う
        for dirpath, _, filenames in os.walk(package_root_dir):
            for filename in filenames:
                if filename.endswith('.py'):
                    file_path = os.path.join(dirpath, filename)
                    namespace, symbols_dependencies = self.dependencies_analyzer.analyze(file_path)
                    # NOTE: `ISymbolInfo`と`PythonSymbolInfo`の問題で，`type: ignore`している。
                    overall_dependencies[namespace] = symbols_dependencies  # type: ignore
        
        # 依存関係をDAGに変換
        dag: Dict[str, list[str]] = {}
        for namespace, dependencies in overall_dependencies.items():
            for symbol_name, dependent_symbol_infos in dependencies.items():
                symbol_info_str = PythonSymbolInfo(namespace, symbol_name).stringify()
                dag[symbol_info_str] = [dependent_symbol_info.stringify() for dependent_symbol_info in dependent_symbol_infos]
                    
        return dag





