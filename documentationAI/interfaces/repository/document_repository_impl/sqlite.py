import sqlite3
from documentationAI.domain.models.document import Document
from documentationAI.domain.models.symbol import ISymbolId
from documentationAI.domain.repositories.interfaces import IDocumentRepository
from documentationAI.domain.services.analyzer import IAnalyzerHelper


class SQLiteDocumentRepositoryImpl(IDocumentRepository):

    def __init__(self, sqlite_db_path: str, helper: IAnalyzerHelper):
        self.helper = helper

        self.conn = sqlite3.connect(sqlite_db_path)
        cursor = self.conn.cursor()

        cursor.execute("""
CREATE TABLE IF NOT EXISTS versions (
    version INTEGER,
    created_at TEXT,
    UNIQUE(version)
);
""")
        cursor.execute("""
CREATE TABLE IF NOT EXISTS documents (
    symbol_id VARCHAR(255),
    exec_version INTEGER,
    content TEXT,
    succeeded INTEGER,
    PRIMARY KEY (symbol_id, exec_version),
    FOREIGN KEY (exec_version) REFERENCES versions(version)   
);
""")
        cursor.execute("""
CREATE TABLE IF NOT EXISTS symbol_dependencies (
    symbol_id VARCHAR(255),
    exec_version INTEGER,
    dependency_symbol_id VARCHAR(255),
    PRIMARY KEY (symbol_id, exec_version, dependency_symbol_id),
    FOREIGN KEY (symbol_id, exec_version) REFERENCES documents(symbol_id, exec_version)
);
""")
        # バージョンをインクリメントする
        new_version = self._get_current_version() + 1
        cursor.execute("""
INSERT INTO versions (version, created_at) VALUES (?, datetime('now', 'localtime'));
""", (new_version,))
        
    
    def get_by_symbol_id(self, symbol_id: ISymbolId) -> Document|None:
        cursor = self.conn.cursor()
        exec_version = self._get_current_version()
        # Documentの基本情報を取得するクエリ
        cursor.execute("""
SELECT  d.content, d.succeeded, v.created_at
    FROM documents AS d
    JOIN versions AS v ON d.exec_version = v.version
    WHERE d.symbol_id = ? AND d.exec_version = ?;
""", (symbol_id.stringify(), exec_version))
        
        result = cursor.fetchone()

        if result:
            content, succeeded, _ = result
            # Documentのシンボルの依存関係を取得するクエリ
            cursor.execute("""
SELECT dependency_symbol_id
    FROM symbol_dependencies
    WHERE symbol_id = ? AND exec_version = ?;
""", (symbol_id.stringify(), exec_version))
            dependencies: list[ISymbolId] = []
            for dependency_symbol_id_str in cursor.fetchall():
                dependencies.append(self.helper.parse_symbol_id_str(dependency_symbol_id_str[0]))
            
            return Document(
                symbol_id = symbol_id,
                dependencies = dependencies,
                content = str(content),
                succeeded = bool(succeeded),
            )
        else:
            return None
    

    def save(self, document: Document) -> None:
        cursor = self.conn.cursor()
        exec_version = self._get_current_version()
        
        try:            
            cursor.execute("""
INSERT INTO documents
    (symbol_id, exec_version, content, succeeded)
    VALUES (?, ?, ?, ?);
""", (document.get_symbol_id().stringify(), exec_version, document.get_content(), int(document.is_succeeded())))
            
            for dependency_symbol_id in document.get_dependencies():
                cursor.execute("""
INSERT INTO symbol_dependencies
    (symbol_id, exec_version, dependency_symbol_id)
    VALUES (?, ?, ?);
""", (document.get_symbol_id().stringify(), exec_version, dependency_symbol_id.stringify()))
                
                self.conn.commit()
        except Exception as e:
            self.conn.rollback()
            raise e
    

    def close(self) -> None:
        self.conn.close()


    def _get_current_version(self) -> int:
        cursor = self.conn.cursor()
        cursor.execute("""
    SELECT MAX(version) FROM versions;
""")
        result = cursor.fetchone()
        if result:
            if result[0]:
                return int(result[0])
            else:
                return 0
        else:
            return 0


if __name__ == "__main__":
    def debug():
        import os
        from documentationAI.domain.implementation.python.helper import PythonAnalyzerHelper
        from documentationAI.domain.implementation.python.symbol import PythonSymbolId
        # 現在のディレクトリより４階層上
        document_repository = SQLiteDocumentRepositoryImpl(
            sqlite_db_path = os.path.join(os.path.dirname(__file__), "../../../..", "test/test_db.sqlite"),
            helper = PythonAnalyzerHelper()
        )

        document1 = Document(
            symbol_id = PythonSymbolId("test.namespace.hoge", "test_symbol_name"),
            dependencies = [],
            content = "test_document_content",
            succeeded = True
        )
        document2 = Document(
            symbol_id = PythonSymbolId("test.namespace.hoge", "test_symbol_name2"),
            dependencies = [PythonSymbolId("test.namespace.hoge", "test_symbol_name")],
            content = "test_document_content2",
            succeeded = True
        )

        document_repository.save(document1)
        document_repository.save(document2)

        result1 = document_repository.get_by_symbol_id(PythonSymbolId("test.namespace.hoge", "test_symbol_name"))
        if result1:
            print(result1.get_content())
        else:
            print("None")
        result2 = document_repository.get_by_symbol_id(PythonSymbolId("test.namespace.hoge", "test_symbol_name2"))
        if result2:
            print(result2.get_content())
        else:
            print("None")

        document_repository.close()
    
    debug()
