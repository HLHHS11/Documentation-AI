## `Router.register`のドキュメント

`Router.register`メソッドは、`Router`クラスのインスタンスに対して、新しいルートを登録するために使用されます。

### 構文

```python
def register(self, request: str, callback: Callable[[list[str]], None]) -> None:
    ...
```

### パラメータ

- `request` (str): ルートのリクエストパスを表す文字列です。
- `callback` (Callable[[list[str]], None]): ルートに対して実行されるコールバック関数です。この関数は、リクエストパスのパラメータを受け取るリストを引数として受け取ります。

### 戻り値

- なし

### 例

```python
router = Router()
router.register('/home', home_handler)
```

この例では、`/home`というリクエストパスに対して`home_handler`というコールバック関数が登録されます。

### 依存する外部シンボルのドキュメント

このメソッドは、外部のシンボルに依存していません。