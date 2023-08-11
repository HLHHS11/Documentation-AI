## `PythonSymbolInfo.parse`のソース定義

```python
@classmethod
def parse(cls, stringified: str) -> 'PythonSymbolInfo':
    (namespace, symbol_name) = stringified.split(':')
    return cls(namespace, symbol_name)
```

`parse`メソッドは、`PythonSymbolInfo`クラスのクラスメソッドとして定義されています。このメソッドは、文字列を受け取り、`PythonSymbolInfo`オブジェクトを返します。

## 依存する外部シンボルのドキュメント

依存する外部シンボルのドキュメントは以下の通りです。ただし、１つも存在しない場合もあります。

- なし