# `Container.cli`のソース定義ファイル

以下は、`Container.cli`のソース定義ファイルの内容です。

```python
cli = providers.Singleton(CLI, router=router)
```

# `Container.cli`が依存関係にあるシンボルのドキュメント

`Container.cli`は、以下の外部シンボルに依存しています。

## `CLI`

### CLIクラス

`CLI`クラスは、コマンドラインインターフェース（CLI）を提供するためのクラスです。

#### コンストラクタ

##### `__init__(self, router: Router) -> None`

`CLI`クラスのインスタンスを初期化します。

###### パラメータ

- `router`（`Router`）：`Router`クラスのインスタンス

#### メソッド

##### `run(self) -> None`

CLIを実行します。CLIの起動メッセージを表示し、ユーザーからの入力を待ちます。入力されたコマンドを処理するために`handle`メソッドを呼び出します。

##### `handle(self, request: str) -> None`

入力されたコマンドを処理します。指定されたコマンドを`router`に渡し、対応するハンドラーを呼び出します。

###### パラメータ

- `request`（`str`）：入力されたコマンド

##### `_exit(self, params: list[str]) -> None`

アプリケーションを終了します。終了メッセージを表示し、`running`フラグを`False`に設定します。

###### パラメータ

- `params`（`list[str]`）：パラメータのリスト

##### 依存関係

`CLI`クラスは`Router`クラスに依存しています。以下の外部シンボルのドキュメントを参照してください。

## `Router`

### Routerクラス

`Router`クラスは、リクエストを処理するためのルーティング機能を提供します。

#### ドキュメント

このセクションでは、`Router`クラスが依存している外部シンボルのドキュメントを提供します。ただし、依存するシンボルが存在しない場合もあります。

依存する外部シンボルはありません。