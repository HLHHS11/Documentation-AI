from documentationAI.domain.models.code_analyzer.abc import ICodeAnalyzer
from documentationAI.utils.topological_sort import topological_sort


# NOTE: `ICodeAnalyzer`が提供する機能に対して目新しい機能はないが，こちらは実装クラスである点がメリットと考えられる。
#       すなわち，抽象クラスを扱う役割をこのクラスが引き受けることで，外側のレイヤからは抽象クラスを意識する必要がなくなる。（常に実装クラスを呼び出せば良い）
class CodeAnalyzeService:

    def __init__(self, code_analyzer: ICodeAnalyzer) -> None:
        self.code_analyzer = code_analyzer
    

    def resolve_dependencies(self, package_root_dir: str) -> list[str]:
        dependencies = self.code_analyzer.generate_dag(package_root_dir)
        resolved = topological_sort(dependencies)
        return resolved
