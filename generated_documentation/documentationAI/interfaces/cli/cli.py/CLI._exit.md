## `CLI._exit`のソース定義

```python
def _exit(self, params: list[str]) -> None:
    print('Goodbye!')
    self.running = False
```

この関数は、`CLI`クラスの`_exit`メソッドを定義しています。このメソッドは、引数として文字列のリスト`params`を受け取ります。

関数の動作は以下の通りです。

1. `'Goodbye!'`というメッセージを表示します。
2. `self.running`を`False`に設定します。

## 依存する外部シンボルのドキュメント

この関数は外部シンボルに依存していません。