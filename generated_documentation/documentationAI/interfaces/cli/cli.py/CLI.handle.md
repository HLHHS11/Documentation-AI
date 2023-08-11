## `CLI.handle`のソース定義

```python
def handle(self, request: str) -> None:
    self.router.handle(request, [])
```

## `CLI.handle`の依存関係

`CLI.handle`メソッドは、`self.router.handle`メソッドに依存しています。

## 依存する外部シンボルのドキュメント

依存する外部シンボルのドキュメントは以下の通りです。

- `self.router.handle`: リクエストを処理するためのメソッドです。