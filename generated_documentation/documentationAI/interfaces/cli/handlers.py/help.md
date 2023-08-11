## `help`関数

`help`関数は、CLI（Command Line Interface）のコマンド一覧を表示するために使用されます。

### パラメータ

- `params`（リスト[str]）：コマンドのパラメータのリスト。

### 返り値

- `None`：何も返しません。

### 使用例

```python
help([])
```

### 利用可能なコマンド

以下のコマンドが利用可能です。

- `generate documentation`：特定のコードファイルのドキュメントを生成します。
- `optimize code`：コードの最適化の提案を行います。
- `generate test cases`：特定のコードファイルのテストケースを生成します。
- `help`：利用可能なコマンドを表示します。
- `exit`：CLIを終了します。

### 依存関係

`help`関数は、外部の依存関係を持ちません。