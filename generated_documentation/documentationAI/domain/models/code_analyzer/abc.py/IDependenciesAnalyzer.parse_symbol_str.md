## `IDependenciesAnalyzer.parse_symbol_str`のソース定義ファイル

```python
@abc.abstractmethod
def parse_symbol_str(self, symbol_str: str) -> ISymbolInfo:
    pass
```

## `IDependenciesAnalyzer.parse_symbol_str`が依存関係にあるシンボルのドキュメント

依存する外部シンボルのドキュメントは以下の通りである。ただし、１つも存在しない場合もあり得る。