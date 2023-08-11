# `Container.routes`のドキュメント

`Container.routes`は、`routes`という名前の辞書オブジェクトです。この辞書は、特定の操作をキーとし、それに対応する関数オブジェクトを値として持ちます。

## ソース定義ファイル

`Container.routes`のソース定義ファイルは以下の通りです。

```python
routes = providers.Dict(routes)
```

## 依存関係

`Container.routes`は、外部シンボル`documentationAI.interfaces.cli.handlers:routes`に依存しています。

## 依存する外部シンボルのドキュメント

### documentationAI.interfaces.cli.handlers:routes

`routes`は、文字列キーと関数オブジェクトのペアを持つ辞書です。各キーは特定の操作を表し、対応する関数はその操作を実行します。

以下は`routes`に含まれるキーとそれに対応する関数の一覧です。

- `help`: ヘルプ情報を表示する関数
- `documentation`: ドキュメンテーションを表示する関数
- `optimize_code`: コードを最適化する関数
- `generate_test_cases`: テストケースを生成する関数
- `exit`: プログラムを終了する関数

依存する外部シンボルのドキュメントはありません。