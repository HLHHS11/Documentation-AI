## `PythonDependenciesAnalyzer.parse_symbol_str`のソース定義

```python
def parse_symbol_str(self, symbol_str: str) -> PythonSymbolInfo:
    result = self.parser([symbol_str], 'GetSymbolInfo')
    return result
```

## `PythonDependenciesAnalyzer.parse_symbol_str`が依存関係にあるシンボルのドキュメント

依存する外部シンボルのドキュメントは以下の通りである。ただし、１つも存在しない場合もあり得る。