## `PythonSymbolInfo.stringify`のソース定義

```python
def stringify(self) -> str:
    return f'{self.namespace}:{self.symbol_name}'
```

この関数は、`PythonSymbolInfo`クラスのメソッドであり、文字列を返します。返される文字列は、`self.namespace`と`self.symbol_name`をコロンで結合したものです。

## 依存する外部シンボルのドキュメント

この関数は、外部のシンボルには依存しません。