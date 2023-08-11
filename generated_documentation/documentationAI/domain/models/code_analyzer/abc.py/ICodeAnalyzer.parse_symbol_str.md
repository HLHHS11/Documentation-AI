## `ICodeAnalyzer.parse_symbol_str`のソース定義ファイル

```python
@abc.abstractmethod
def parse_symbol_str(self, symbol_str: str) -> ISymbolInfo:
    pass
```

`ICodeAnalyzer.parse_symbol_str`は、`abc`モジュールの`abstractmethod`デコレータを使用して抽象メソッドとして定義されています。このメソッドは、`symbol_str`という文字列型の引数を受け取り、`ISymbolInfo`型の戻り値を返します。

## `ICodeAnalyzer.parse_symbol_str`が依存関係にあるシンボルのドキュメント

依存する外部シンボルのドキュメントは以下の通りです。ただし、１つも存在しない場合もあります。