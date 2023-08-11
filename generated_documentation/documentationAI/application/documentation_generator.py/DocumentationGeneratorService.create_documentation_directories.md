## `DocumentationGeneratorService.create_documentation_directories`のソース定義ファイル

```python
def create_documentation_directories(self, root_dir: str, package_name: str) -> None:
    package_root_dir = os.path.join(root_dir, package_name)
    documentation_root_dir = os.path.join(root_dir, 'generated_documentation', package_name)
    self._create_directory_structure(package_root_dir, documentation_root_dir)
```

`DocumentationGeneratorService.create_documentation_directories`は、指定されたルートディレクトリとパッケージ名を使用して、ドキュメントのディレクトリ構造を作成するメソッドです。

### パラメータ

- `root_dir` (str): ドキュメントのルートディレクトリのパス
- `package_name` (str): パッケージの名前

### 戻り値

- `None`

## 依存する外部シンボルのドキュメント

このメソッドは、`_create_directory_structure`メソッドを使用していますが、その他の外部シンボルには依存していません。