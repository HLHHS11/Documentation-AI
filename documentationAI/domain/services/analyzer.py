import abc
from typing import Dict, Tuple

from documentationAI.domain.models.symbol import ISymbolId


class IAnalyzerHelper(abc.ABC):

    @abc.abstractmethod
    def parse_symbol_id_str(self, symbol_id_str: str) -> ISymbolId:
        pass


    @abc.abstractmethod
    def abspath_to_namespace(self, module_abs_path: str, package_root_path: str) -> str:    
        pass

    @abc.abstractmethod
    def namespace_to_abspath(self, namespace: str, package_root_dir: str) -> str:
        pass

    @abc.abstractmethod
    def get_symbol_def(self, symbol_id: ISymbolId, package_root_dir: str) -> str:
        pass


class IModuleAnalyzer(abc.ABC):

    def __init__(
        self,
        helper: IAnalyzerHelper
    ):
        self.helper = helper

    @abc.abstractmethod
    def analyze(self, module_path: str, package_root_dir: str, package_name: str) -> Tuple[str, Dict[str, list[ISymbolId]]]:
        pass


class IPackageAnalyzer(abc.ABC):

    @abc.abstractmethod
    def generate_dag(self, package_root_dir: str, package_name: str) -> Dict[ISymbolId, list[ISymbolId]]:
        pass
    
    @abc.abstractmethod
    def generate_reversed_dag_from_dag(self, dag: Dict[ISymbolId, list[ISymbolId]]) -> Dict[ISymbolId, list[ISymbolId]]:
        pass
