## `CLI.run`のソース定義ファイル

```python
def run(self) -> None:
    print('Welcome to Documentation-AI!')
    print("Type 'help' for available commands or 'exit' to quit.")
    while self.running:
        command = input('>> ')
        self.handle(command)
```

`CLI.run`は、`CLI`クラスのメソッドであり、コマンドラインインターフェース（CLI）の実行を行います。

このメソッドは、以下の手順で実行されます。

1. `'Welcome to Documentation-AI!'`というメッセージを表示します。
2. `'Type 'help' for available commands or 'exit' to quit.'`というメッセージを表示します。
3. `self.running`が`True`である間、以下の処理を繰り返します。
   - ユーザーからの入力を受け取り、`command`に代入します。
   - `self.handle(command)`を呼び出します。

## 依存する外部シンボルのドキュメント

このメソッドは、外部のシンボルに依存している場合がありますが、現在の情報ではその詳細はわかりません。