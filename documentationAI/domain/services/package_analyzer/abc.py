import abc
from typing import Dict, Tuple

from documentationAI.domain.models.document.symbol_info import ISymbolInfo

class IAnalyzerHelper(abc.ABC):

    @abc.abstractmethod
    def parse_symbol_str(self, symbol_str: str) -> ISymbolInfo:
        pass


    @abc.abstractmethod
    def abspath_to_namespace(self, module_abs_path: str, package_root_path: str) -> str:    
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
    def analyze(self, module_path: str, package_root_dir: str, package_name: str) -> Tuple[str, Dict[str, list[ISymbolInfo]]]:
        pass

    @abc.abstractmethod
    def get_symbol_impl(self, file_path: str, symbol_name: str) -> str:
        pass

    @abc.abstractmethod
    def get_module_impl(self, file_path: str) -> str:
        pass


class IPackageAnalyzer(abc.ABC):

    @abc.abstractmethod
    def generate_dag(self, package_root_dir: str, package_name: str) -> Dict[str, list[str]]:
        pass
