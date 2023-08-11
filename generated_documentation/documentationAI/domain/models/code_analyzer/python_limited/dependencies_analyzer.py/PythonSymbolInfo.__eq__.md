## `PythonSymbolInfo.__eq__`のソース定義

```python
def __eq__(self, other: object) -> bool:
    if isinstance(other, PythonSymbolInfo):
        return self.namespace == other.namespace and self.symbol_name == other.symbol_name
    else:
        return False
```

## `PythonSymbolInfo.__eq__`が依存関係にあるシンボルのドキュメント

依存する外部シンボルのドキュメントは以下の通りである。ただし、１つも存在しない場合もあり得る。