from typing import NamedTuple, Dict, Callable

from documentationAI.domain.models.code_analyzer.abc import ICodeAnalyzer
# from documentationAI.domain.models.code_analyzer.python_limited.dependencies_analyzer import IDependenciesAnalyzer
from documentationAI.utils.topological_sort import topological_sort
from documentationAI.domain.models.code_analyzer.abc import ISymbolInfo


class DependenciesNamedTuple(NamedTuple):
    dependencies: Dict[str, list[str]]
    resolved: list[str]

# NOTE: `ICodeAnalyzer`が提供する機能に対して目新しい機能はないが，こちらは実装クラスである点がメリットと考えられる。
#       すなわち，抽象クラスを扱う役割をこのクラスが引き受けることで，外側のレイヤからは抽象クラスを意識する必要がなくなる。（常に実装クラスを呼び出せば良い）
class CodeAnalyzeService:

    def __init__(
        self, code_analyzer: ICodeAnalyzer,
        parser: Callable[[list[str], str], ISymbolInfo|str],
        # dependencies_analyzer: IDependenciesAnalyzer
    ) -> None:
        self.code_analyzer = code_analyzer
        self.parser = parser
        # self.dependencies_analyzer = dependencies_analyzer
    

    def resolve_dependencies(self, package_root_dir: str) -> DependenciesNamedTuple:
        dependencies_map = self.code_analyzer.generate_dag(package_root_dir)
        resolved = topological_sort(dependencies_map)
        return DependenciesNamedTuple(dependencies_map, resolved)
    

    def parse_symbol_str(self, symbol_str: str):
        return self.code_analyzer.parse_symbol_str(symbol_str)

