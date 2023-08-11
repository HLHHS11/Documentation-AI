## `IDependenciesAnalyzer`のソース定義ファイル

```python
class IDependenciesAnalyzer(abc.ABC):

    @abc.abstractmethod
    def analyze(self, file_path: str) -> Tuple[str, Dict[str, list[ISymbolInfo]]]:
        pass

    @abc.abstractmethod
    def parse_symbol_str(self, symbol_str: str) -> ISymbolInfo:
        pass

    @abc.abstractmethod
    def get_symbol_definition(self, file_path: str, symbol_name: str) -> str:
        pass

    @abc.abstractmethod
    def get_file_contents(self, file_path: str) -> str:
        pass
```

## `IDependenciesAnalyzer`が依存関係にあるシンボルのドキュメント

依存する外部シンボルのドキュメントは以下の通りである。ただし、１つも存在しない場合もあり得る。