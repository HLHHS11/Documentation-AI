## `PythonDependenciesAnalyzer._get_top_level_symbol_nodes`のソース定義

```python
def _get_top_level_symbol_nodes(self, tree: ast.AST) -> list[ast.AST]:
    top_level_symbol_nodes: list[ast.AST] = []
    function_def_nodes: set[ast.FunctionDef | ast.AsyncFunctionDef] = set()
    for node in ast.walk(tree):
        if isinstance(node, (ast.FunctionDef, ast.ClassDef, ast.AsyncFunctionDef, ast.AnnAssign, ast.AugAssign, ast.Assign)):
            for function_def_node in function_def_nodes:
                if node in ast.walk(function_def_node):
                    break
            else:
                if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
                    function_def_nodes.add(node)
                top_level_symbol_nodes.append(node)
                continue
    return top_level_symbol_nodes
```

## `PythonDependenciesAnalyzer._get_top_level_symbol_nodes`が依存関係にあるシンボルのドキュメント

依存する外部シンボルのドキュメントは以下の通りである。ただし、１つも存在しない場合もあり得る。