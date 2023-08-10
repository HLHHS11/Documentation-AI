import abc
from typing import Dict, Tuple

class ISymbolInfo(abc.ABC):

    @abc.abstractmethod
    def stringify(self) -> str:
        pass
    
    @classmethod
    @abc.abstractmethod
    def parse(cls, stringified: str) -> 'ISymbolInfo':
        pass


class IDependenciesAnalyzer(abc.ABC):

    @abc.abstractmethod
    def analyze(self, file_path: str) -> Tuple[str, Dict[str, list[ISymbolInfo]]]:
        pass

    @abc.abstractmethod
    def parse_symbol_str(self, symbol_str: str) -> ISymbolInfo:
        pass


class ICodeAnalyzer(abc.ABC):

    def __init__(
        self, dependencies_analyzer: IDependenciesAnalyzer
    ):
        self.dependencies_analyzer = dependencies_analyzer

    @abc.abstractmethod
    def generate_dag(self, package_root_dir: str) -> Dict[str, list[str]]:
        pass

    @abc.abstractmethod
    def parse_symbol_str(self, symbol_str: str) -> ISymbolInfo:
        pass
