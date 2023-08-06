import abc

class CodeAnalyzer(abc.ABC):
    @abc.abstractmethod
    def analyze(self, code: str) -> None:
        pass