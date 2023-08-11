## `ICodeAnalyzer`のソース定義ファイル

```python
class ICodeAnalyzer(abc.ABC):

    def __init__(self, dependencies_analyzer: IDependenciesAnalyzer):
        self.dependencies_analyzer = dependencies_analyzer

    @abc.abstractmethod
    def generate_dag(self, package_root_dir: str) -> Dict[str, list[str]]:
        pass

    @abc.abstractmethod
    def parse_symbol_str(self, symbol_str: str) -> ISymbolInfo:
        pass
```

## `ICodeAnalyzer`が依存関係にあるシンボルのドキュメント

依存する外部シンボルのドキュメントは以下の通りである。ただし、１つも存在しない場合もあり得る。