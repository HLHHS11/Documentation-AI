## `PythonDependenciesAnalyzer.get_symbol_definition`のソース定義ファイル

```python
def get_symbol_definition(self, file_path: str, symbol_name: str) -> str:
    with open(file_path, 'r') as file:
        tree = ast.parse(file.read())
    for node in ast.walk(tree):
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
            if node.name == symbol_name.split('.')[-1]:
                return ast.unparse(node)
        elif isinstance(node, (ast.AnnAssign, ast.AugAssign)):
            if node.target.id == symbol_name.split('.')[-1]:
                return ast.unparse(node)
        elif isinstance(node, ast.Assign):
            if node.targets[0].id == symbol_name.split('.')[-1]:
                return ast.unparse(node)
    return ''
```

## `PythonDependenciesAnalyzer.get_symbol_definition`が依存関係にあるシンボルのドキュメント

依存する外部シンボルのドキュメントは以下の通りである。ただし、１つも存在しない場合もあり得る。