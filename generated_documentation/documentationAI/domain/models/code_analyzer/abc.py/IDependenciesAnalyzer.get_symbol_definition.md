## `IDependenciesAnalyzer.get_symbol_definition`のソース定義ファイル

```python
@abc.abstractmethod
def get_symbol_definition(self, file_path: str, symbol_name: str) -> str:
    pass
```

## `IDependenciesAnalyzer.get_symbol_definition`が依存関係にあるシンボルのドキュメント

依存する外部シンボルのドキュメントは以下の通りである。ただし、１つも存在しない場合もあり得る。