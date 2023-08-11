## `ISymbolInfo.__init__`のソース定義ファイル

```python
def __init__(self, namespace: str, symbol_name: str):
    self.namespace: str = namespace
    self.symbol_name: str = symbol_name
```

`ISymbolInfo.__init__`は、`ISymbolInfo`クラスのコンストラクタです。このメソッドは、`namespace`と`symbol_name`という2つの引数を受け取ります。

### パラメータ

- `namespace` (str): シンボルの名前空間を表す文字列です。
- `symbol_name` (str): シンボルの名前を表す文字列です。

### 戻り値

なし

## 依存する外部シンボルのドキュメント

`ISymbolInfo.__init__`メソッドは、外部のシンボルには依存していません。