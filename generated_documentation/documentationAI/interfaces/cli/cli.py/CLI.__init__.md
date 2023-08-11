# CLI.__init__のソース定義ファイル

以下は、`CLI.__init__`のソース定義ファイルです。

```python
def __init__(self, router: Router) -> None:
    self.router = router
    self.running = True
    self.router.register('exit', self._exit)
```

# CLI.__init__が依存関係にあるシンボルのドキュメント

以下は、`CLI.__init__`が依存関係にあるシンボルのドキュメントです。

## documentationAI.interfaces.cli.router:Router

### 依存する外部シンボルのドキュメント

このセクションでは、`Router`クラスが依存している外部シンボルのドキュメントを提供します。ただし、依存するシンボルが存在しない場合もあります。

依存する外部シンボルはありません。