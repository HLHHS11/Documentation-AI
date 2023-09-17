import abc


class ISymbolId(abc.ABC):

    def __init__(self, namespace: str, symbol_name: str):
        self.namespace: str = namespace
        self.symbol_name: str = symbol_name

    @abc.abstractmethod
    def stringify(self) -> str:
        pass
    
    @classmethod
    @abc.abstractmethod
    def parse(cls, stringified: str) -> 'ISymbolId':
        pass

    @abc.abstractmethod
    def __eq__(self, other: object) -> bool:
        pass

    @abc.abstractmethod
    def __hash__(self) -> int:
        pass

    @abc.abstractmethod
    def __str__(self) -> str:
        pass


class ISymbol(abc.ABC):

    def __init__(
        self,
        id: ISymbolId,
        definition: str,
        dependencies: list[ISymbolId]
    ):
        self.id = id
        self.definition = definition
        self.dependencies = dependencies
    