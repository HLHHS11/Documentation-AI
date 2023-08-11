## `Router.handle`のドキュメント

`Router.handle`メソッドは、リクエストを処理するためのメソッドです。

### パラメータ

- `request` (str): 処理するリクエストの種類を示す文字列です。
- `params` (list[str]): リクエストに関連するパラメータのリストです。

### 戻り値

このメソッドは戻り値を返しません。

### 例外

このメソッドは例外を発生させません。

### 依存関係

このメソッドは以下の外部シンボルに依存しています。

- `self.routes`: リクエストとハンドラのマッピングを保持する辞書です。

### 例

```python
router = Router()
router.handle("get", ["param1", "param2"])
```

### 注意事項

- `request`が`self.routes`に含まれていない場合、"Invalid command. Type 'help' for available commands."というメッセージが表示されます。