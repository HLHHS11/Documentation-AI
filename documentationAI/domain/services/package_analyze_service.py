from typing import NamedTuple, Dict

from documentationAI.domain.models.package_analyzer.abc import IAnalyzerHelper, IPackageAnalyzer
from documentationAI.utils.topological_sort import topological_sort


class DependenciesNamedTuple(NamedTuple):
    dependencies: Dict[str, list[str]]
    resolved: list[str]

# NOTE: `ICodeAnalyzer`が提供する機能に対して目新しい機能はないが，こちらは実装クラスである点がメリットと考えられる。
#       すなわち，抽象クラスを扱う役割をこのクラスが引き受けることで，外側のレイヤからは抽象クラスを意識する必要がなくなる。（常に実装クラスを呼び出せば良い）
class PackageAnalyzeService:

    def __init__(
        self,
        package_analyzer: IPackageAnalyzer,
        helper: IAnalyzerHelper
    ) -> None:
        self.package_analyzer = package_analyzer
        self.helper = helper
    

    def resolve_dependencies(self, package_root_dir: str) -> DependenciesNamedTuple:
        dependencies_map = self.package_analyzer.generate_dag(package_root_dir)
        resolved = topological_sort(dependencies_map)
        return DependenciesNamedTuple(dependencies_map, resolved)


