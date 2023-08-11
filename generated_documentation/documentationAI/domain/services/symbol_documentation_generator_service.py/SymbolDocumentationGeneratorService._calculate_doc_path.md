## `SymbolDocumentationGeneratorService._calculate_doc_path`のソース定義ファイル

```python
def _calculate_doc_path(self, root_dir: str, symbol_str: str) -> str:
    file_path = self._get_file_path(symbol_str, root_dir)
    relative_path = os.path.relpath(file_path, root_dir)
    symbol_name = self._get_symbol_info(symbol_str).symbol_name
    doc_path = os.path.join(root_dir, 'generated_documentation/', relative_path, f'{symbol_name}.md')
    return doc_path
```

`SymbolDocumentationGeneratorService._calculate_doc_path`は、指定されたルートディレクトリとシンボルの文字列から、ドキュメントのパスを計算するためのメソッドです。

### パラメータ

- `root_dir` (str): ルートディレクトリのパス
- `symbol_str` (str): シンボルの文字列

### 返り値

- `doc_path` (str): ドキュメントのパス

## 依存する外部シンボルのドキュメント

依存する外部シンボルのドキュメントは以下の通りです。ただし、１つも存在しない場合もあります。