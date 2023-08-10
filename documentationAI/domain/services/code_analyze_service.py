from documentationAI.domain.models.code_analyzer.abc import ICodeAnalyzer
from documentationAI.utils.topological_sort import topological_sort


class CodeAnalyzeService:

    def __init__(self, code_analyzer: ICodeAnalyzer) -> None:
        self.code_analyzer = code_analyzer
    

    def resolve_dependencies(self, package_root_dir: str) -> list[str]:
        dependencies = self.code_analyzer.generate_dag(package_root_dir)
        resolved = topological_sort(dependencies)
        return resolved
