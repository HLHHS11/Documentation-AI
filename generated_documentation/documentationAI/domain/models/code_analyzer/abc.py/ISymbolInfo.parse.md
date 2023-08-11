## `ISymbolInfo.parse`のソース定義ファイル

```python
@classmethod
@abc.abstractmethod
def parse(cls, stringified: str) -> 'ISymbolInfo':
    pass
```

`ISymbolInfo.parse`は、`ISymbolInfo`クラスのクラスメソッドであり、`stringified`という名前の文字列型の引数を受け取り、`ISymbolInfo`型のオブジェクトを返す抽象メソッドです。

## `ISymbolInfo.parse`の依存関係にあるシンボルのドキュメント

`ISymbolInfo.parse`は、外部シンボルに依存することがあります。依存する外部シンボルのドキュメントは以下の通りです。

（依存する外部シンボルのドキュメントが存在する場合は、ここに記載してください。存在しない場合は、その旨を記載してください。）