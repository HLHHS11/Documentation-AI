## `PythonDependenciesAnalyzer._collect_imports`のソース定義ファイル

```python
def _collect_imports(self, tree: ast.AST) -> list[ast.Import | ast.ImportFrom]:
    import_statements: list[ast.Import | ast.ImportFrom] = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Import | ast.ImportFrom):
            import_statements.append(node)
    return import_statements
```

## `PythonDependenciesAnalyzer._collect_imports`が依存関係にあるシンボルのドキュメント

依存する外部シンボルのドキュメントは以下の通りである。ただし、１つも存在しない場合もあり得る。