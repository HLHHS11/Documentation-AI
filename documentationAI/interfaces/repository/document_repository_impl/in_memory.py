from typing import Dict

from documentationAI.domain.models.symbol import ISymbolId
from documentationAI.domain.models.document import Document
from documentationAI.domain.repositories.interfaces import IDocumentRepository


class InMemoryDocumentRepositoryImpl(IDocumentRepository):

    def __init__(self):
        self._documents: Dict[str, Document] = {}
    
    def get_by_symbol_id(self, symbol_id: ISymbolId) -> Document|None:
        try:
            return self._documents[symbol_id.stringify()]
        except KeyError:
            return None
    
    def save(self, document: Document) -> None:
        self._documents[document.get_symbol_id().stringify()] = document


if __name__ == "__main__":
    from documentationAI.domain.implementation.python.symbol import PythonSymbolId

    def debug():
        document_repository = InMemoryDocumentRepositoryImpl()

        document1 = Document(
            symbol_id = PythonSymbolId("test.namespace.hoge", "test_symbol_name"),
            dependencies = [],
            content = "test_document_content",
            succeeded = True
        )

        document_repository.save(document1)

        print(document_repository.get_by_symbol_id(PythonSymbolId("test.namespace.hoge", "test_symbol_name")).get_content())

    debug()
