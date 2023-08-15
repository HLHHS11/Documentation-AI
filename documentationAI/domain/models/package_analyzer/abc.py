import abc
from typing import Dict, Tuple


class ISymbolInfo(abc.ABC):

    def __init__(self, namespace: str, symbol_name: str):
        self.namespace: str = namespace
        self.symbol_name: str = symbol_name

    @abc.abstractmethod
    def stringify(self) -> str:
        pass
    
    @classmethod
    @abc.abstractmethod
    def parse(cls, stringified: str) -> 'ISymbolInfo':
        pass

    @abc.abstractmethod
    def __eq__(self, other: object) -> bool:
        pass

    @abc.abstractmethod
    def __str__(self) -> str:
        pass


class IAnalyzerHelper(abc.ABC):

    @abc.abstractmethod
    def parse_symbol_str(self, symbol_str: str) -> ISymbolInfo:
        pass


    @abc.abstractmethod
    def abspath_to_namespace(self, abs_path: str, root_dir: str) -> str:    
        pass

    @abc.abstractmethod
    def namespace_to_abspath(self, namespace: str, root_dir: str) -> str:
        pass


class IModuleAnalyzer(abc.ABC):

    def __init__(
        self,
        helper: IAnalyzerHelper
    ):
        self.helper = helper

    @abc.abstractmethod
    def analyze(self, file_path: str) -> Tuple[str, Dict[str, list[ISymbolInfo]]]:
        pass

    @abc.abstractmethod
    def get_symbol_impl(self, file_path: str, symbol_name: str) -> str:
        pass

    @abc.abstractmethod
    def get_module_impl(self, file_path: str) -> str:
        pass


class IPackageAnalyzer(abc.ABC):

    def __init__(
        self,
        dependencies_analyzer: IModuleAnalyzer,
        helper: IAnalyzerHelper
    ):
        self.dependencies_analyzer = dependencies_analyzer
        self.helper = helper

    @abc.abstractmethod
    def generate_dag(self, package_root_dir: str) -> Dict[str, list[str]]:
        pass
