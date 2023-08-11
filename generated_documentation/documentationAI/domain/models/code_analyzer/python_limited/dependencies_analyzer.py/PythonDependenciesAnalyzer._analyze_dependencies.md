## `PythonDependenciesAnalyzer._analyze_dependencies`のソース定義ファイル

```python
def _analyze_dependencies(self, top_level_symbol_nodes: list[ast.AST], import_nodes: list[ast.Import | ast.ImportFrom]) -> Dict[str, list[PythonSymbolInfo]]:
    symbols_dependencies: Dict[str, list[PythonSymbolInfo]] = {}
    import_symbols: list[Tuple[str, str, bool]] = []
    for node in import_nodes:
        if isinstance(node, ast.Import):
            for alias in node.names:
                import_symbols.append((alias.name, alias.asname or alias.name, True))
        else:
            for alias in node.names:
                import_symbols.append((node.module, alias.name, False))
    class_def_nodes: set[ast.ClassDef] = set()
    for node in top_level_symbol_nodes:
        if isinstance(node, ast.ClassDef):
            symbol_name = node.name
            class_def_nodes.add(node)
        elif isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            symbol_name = node.name
            for class_def_node in class_def_nodes:
                if node in ast.walk(class_def_node):
                    symbol_name = f'{class_def_node.name}.{node.name}'
                    break
        elif isinstance(node, (ast.AnnAssign, ast.AugAssign)):
            symbol_name = node.target.id if isinstance(node.target, ast.Name) else None
            for class_def_node in class_def_nodes:
                if node in ast.walk(class_def_node):
                    symbol_name = f'{class_def_node.name}.{symbol_name}'
                    break
        elif isinstance(node, ast.Assign):
            symbol_name = node.targets[0].id if isinstance(node.targets[0], ast.Name) else None
            for class_def_node in class_def_nodes:
                if node in ast.walk(class_def_node):
                    symbol_name = f'{class_def_node.name}.{symbol_name}'
                    break
        else:
            symbol_name = None
        if symbol_name:
            symbol_infos: list[PythonSymbolInfo] = []
            for child in ast.walk(node):
                if isinstance(child, ast.Name):
                    for (namespace, import_symbol, is_import) in import_symbols:
                        if child.id == import_symbol:
                            dependency = PythonSymbolInfo(namespace, import_symbol if not is_import else '*')
                            if dependency not in symbol_infos:
                                symbol_infos.append(dependency)
            symbols_dependencies[symbol_name] = symbol_infos
    return symbols_dependencies
```

## `PythonDependenciesAnalyzer._analyze_dependencies`が依存する外部シンボルのドキュメント

依存する外部シンボルのドキュメントは以下の通りである。ただし、１つも存在しない場合もあり得る。