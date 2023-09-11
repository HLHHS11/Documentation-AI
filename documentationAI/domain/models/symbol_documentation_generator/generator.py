from documentationAI.settings import OPENAI_API_KEY


# 受け取った情報をもとに，テンプレートを用いて，自然言語AIに投げるべきテキストの形式に変換する，
class SymbolDocumentationGenerator:

    def __init__(self):
        pass

    # TODO: 引数で受け取るべき情報を検討する
    def set_context(
        self,
        symbol_name: str,   # NOTE: 指定が必須
        symbol_definition: str, # NOTE: 指定が必須
        dependency_docs: dict[str, str] = {}
        
    ) -> None:
        # TODO: implement
    

    def generate(self) -> str:
        # TODO: implement