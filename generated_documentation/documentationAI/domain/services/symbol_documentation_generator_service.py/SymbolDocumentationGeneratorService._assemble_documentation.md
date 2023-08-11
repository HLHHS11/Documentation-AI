## `SymbolDocumentationGeneratorService._assemble_documentation`

`SymbolDocumentationGeneratorService._assemble_documentation`は、指定されたシンボルのドキュメントを組み立てるためのメソッドです。

### パラメータ

- `symbol_name` (str): シンボルの名前
- `symbol_definition` (str): シンボルの定義
- `dependency_docs` (Dict[str, str]): 依存関係にあるシンボルのドキュメントを格納した辞書

### 戻り値

- `assembled_doc` (str): 組み立てられたドキュメント

### ソースコード

```python
def _assemble_documentation(self, symbol_name: str, symbol_definition: str, dependency_docs: Dict[str, str]) -> str:
    assembled_doc = f'\n# `{symbol_name}`のソース定義ファイルは以下の通り。\n<pythonscript id="{symbol_name}>\n{symbol_definition}\n</pythonscript>\n# `{symbol_name}`が依存関係にあるシンボルのドキュメント\n依存する外部シンボルのドキュメントは以下の通りである。ただし，１つも存在しない場合もあり得る。\n'
    for (dependency_symbol_str, dependency_doc) in dependency_docs.items():
        to_be_appended = f'---\n## {dependency_symbol_str}\n<dependencydoc id="{dependency_symbol_str}">\n{dependency_doc}\n</dependencydoc>\n---\n\n'
        assembled_doc += to_be_appended
    return assembled_doc
```

### 使用例

```python
symbol_name = "example_symbol"
symbol_definition = "def example_function():\n    pass"
dependency_docs = {
    "dependency_symbol1": "This is the documentation for dependency_symbol1.",
    "dependency_symbol2": "This is the documentation for dependency_symbol2."
}

documentation = _assemble_documentation(symbol_name, symbol_definition, dependency_docs)
print(documentation)
```

### 出力例

```
# `example_symbol`のソース定義ファイルは以下の通り。
<pythonscript id="example_symbol">
def example_function():
    pass
</pythonscript>
# `example_symbol`が依存関係にあるシンボルのドキュメント
依存する外部シンボルのドキュメントは以下の通りである。ただし，１つも存在しない場合もあり得る。

---
## dependency_symbol1
<dependencydoc id="dependency_symbol1">
This is the documentation for dependency_symbol1.
</dependencydoc>
---

---
## dependency_symbol2
<dependencydoc id="dependency_symbol2">
This is the documentation for dependency_symbol2.
</dependencydoc>
---
```