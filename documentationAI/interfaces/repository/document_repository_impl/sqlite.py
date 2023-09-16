from requests import Session
import sqlite3

from documentationAI.domain.repositories.interfaces import IDocumentRepository


class SQLiteDocumentRepositoryImpl(IDocumentRepository):

    def __init__(self, sqlite_db_path: str):
        self.connection = sqlite3.connect(sqlite_db_path)

