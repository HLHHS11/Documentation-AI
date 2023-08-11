## `namespace_to_relativepath`のソース定義ファイル

```python
def namespace_to_relativepath(namespace: str) -> str:
    return namespace.replace('.', os.sep) + '.py'
```

`namespace_to_relativepath`関数は、与えられた名前空間を相対パスに変換するための関数です。名前空間はドットで区切られた文字列で表され、それをOSのディレクトリセパレータに置き換え、拡張子`.py`を追加します。

## 依存する外部シンボルのドキュメント

依存する外部シンボルのドキュメントは以下の通りです。ただし、１つも存在しない場合もあります。

- 依存する外部シンボルが存在しません。