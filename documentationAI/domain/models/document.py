# Aggregate root

from documentationAI.domain.models.symbol import ISymbolId

# TODO: そもそもこのクラスは必要なのか検討する
class Document:
    # TODO: implement
    def __init__(
        self,
        symbol_id: ISymbolId,
        # dependencies: list[ISymbolId],
        content: str,
        succeeded: bool,
    ):
        self._symbol_id = symbol_id
        # self._dependencies = dependencies
        self._content = content
        self._succeeded = succeeded

    def get_symbol_id(self) -> ISymbolId:
        return self._symbol_id
    
    def get_content(self) -> str:
        return self._content

    def is_succeeded(self) -> bool:
        return self._succeeded
