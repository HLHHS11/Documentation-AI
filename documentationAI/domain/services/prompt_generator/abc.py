import abc
from typing import Dict, Any

# NOTE: `IPromptGenerator`の仕様を統一化するためのインターフェース。引数として利用されることを想定。
class IPromptGeneratorContext(abc.ABC):
    
    @abc.abstractmethod
    def get_as_dict(self) -> Dict[str, Any]:
        pass

    # NOTE: この次にあるようなファクトリメソッドを利用したほうが良いと考えた。
    # @abc.abstractmethod
    # def set_by_dict(self, context_dict: Dict[str, Any]) -> None:
    #     pass

    @classmethod
    @abc.abstractmethod
    def from_dict(cls, context_dict: Dict[str, Any]) -> "IPromptGeneratorContext":
        pass
    


# 受け取った情報をもとに，テンプレートを用いて，自然言語AIに投げるべきテキストの形式に変換する，
class IPromptGenerator(abc.ABC):

    @abc.abstractmethod
    def generate(self, context: IPromptGeneratorContext) -> str:
        pass
