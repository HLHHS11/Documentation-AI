import abc


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
