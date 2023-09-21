import abc

from documentationAI.domain.models.document import Document
from documentationAI.domain.models.symbol import ISymbolId


# TODO: RustのOkのような処理結果をラップする仕組みを使いたい
class IDocumentRepository(abc.ABC):

    @abc.abstractmethod
    def get_by_symbol_id(self, symbol_id: ISymbolId) -> Document|None:
        pass

    @abc.abstractmethod
    def save(self, document: Document) -> None:
        pass

    # TODO: 以下はイメージ。実際に必要かどうかはまた検討するべし。
    # @abc.abstractmethod
    # def get_all(self) -> list[Document]:
    #     pass

    # @abc.abstractmethod
    # def get_by_id(self, id: int) -> Document:
    #     pass

    # @abc.abstractmethod
    # def create(self, document: Document) -> Document:
    #     pass

    # @abc.abstractmethod
    # def update(self, id: int, document: Document) -> Document:
    #     pass

    # @abc.abstractmethod
    # def delete(self, id: int) -> Document:
    #     pass
