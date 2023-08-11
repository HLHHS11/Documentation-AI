# Container.router

`Container.router`は、`Router`クラスのインスタンスを提供するシングルトンプロバイダです。`Router`クラスは、指定されたルート情報を使用してルーティングを行う機能を提供します。

## ソース定義ファイル

```python
router = providers.Singleton(Router, routes=routes)
```

## 依存関係

`Container.router`は以下の外部シンボルに依存しています。

### documentationAI.interfaces.cli.router:Router

`Router`クラスは、ルーティング機能を提供するクラスです。

依存する外部シンボルのドキュメントは以下の通りです。

---

## documentationAI.interfaces.cli.handlers:routes

`routes`は、文字列キーと関数オブジェクトのペアを持つ辞書です。各キーは特定の操作を表し、対応する関数はその操作を実行します。

以下は`routes`に含まれるキーとそれに対応する関数の一覧です。

- `help`: ヘルプ情報を表示する関数
- `documentation`: ドキュメンテーションを表示する関数
- `optimize_code`: コードを最適化する関数
- `generate_test_cases`: テストケースを生成する関数
- `exit`: プログラムを終了する関数

### ソース定義ファイル

```python
routes: Dict[str, Callable[[list[str]], None]] = {'help': help, 'documentation': documentation, 'optimize_code': optimize_code, 'generate_test_cases': generate_test_cases, 'exit': exit}
```

## 依存する外部シンボルのドキュメント

依存する外部シンボルのドキュメントはありません。