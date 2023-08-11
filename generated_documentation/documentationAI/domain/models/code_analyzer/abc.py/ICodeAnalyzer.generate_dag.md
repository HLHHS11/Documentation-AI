## `ICodeAnalyzer.generate_dag`のソース定義ファイル

```python
@abc.abstractmethod
def generate_dag(self, package_root_dir: str) -> Dict[str, list[str]]:
    pass
```

## `ICodeAnalyzer.generate_dag`が依存関係にあるシンボルのドキュメント

依存する外部シンボルのドキュメントは以下の通りです。ただし、１つも存在しない場合もあります。