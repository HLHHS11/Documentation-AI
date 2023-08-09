import abc
from typing import Dict, Tuple

class ISymbolInfo(abc.ABC):

    @abc.abstractmethod
    def stringify(self) -> str:
        pass


class IDependenciesAnalyzer(abc.ABC):

    @abc.abstractmethod
    def analyze(self, file_path: str) -> Tuple[str, Dict[str, list[ISymbolInfo]]]:
        pass


class ICodeAnalyzer(abc.ABC):

    def __init__(
        self, dependencies_analyzer: IDependenciesAnalyzer
    ):
        self.dependencies_analyzer = dependencies_analyzer

    @abc.abstractmethod
    def generate_dag(self, root_dir: str) -> Dict[str, list[str]]:
        pass


