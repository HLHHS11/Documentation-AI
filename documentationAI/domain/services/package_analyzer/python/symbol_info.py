from documentationAI.domain.models.document.symbol_info import ISymbolInfo


class PythonSymbolInfo(ISymbolInfo):

    def __init__(self, namespace: str, symbol_name: str):
        self.namespace: str = namespace
        self.symbol_name: str = symbol_name

    # ネームスペースとシンボル名を:で結合した文字列を返す 
    def stringify(self) -> str:
        return f"{self.namespace}:{self.symbol_name}"
    
    @classmethod
    def parse(cls, stringified: str) -> 'PythonSymbolInfo':
        namespace, symbol_name = stringified.split(':')
        return cls(namespace, symbol_name)

    def __eq__(self, other: object) -> bool:
        if isinstance(other, PythonSymbolInfo):
            return self.namespace == other.namespace and self.symbol_name == other.symbol_name
        else:
            return False
    
    def __str__(self) -> str:
        return f"PythonSymbolInfo(namespace={self.namespace}, symbol_name={self.symbol_name})"
