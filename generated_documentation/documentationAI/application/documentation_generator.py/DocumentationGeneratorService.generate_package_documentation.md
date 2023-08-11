## `DocumentationGeneratorService.generate_package_documentation`のソース定義ファイル

```python
def generate_package_documentation(self, root_dir: str, package_name: str) -> None:
    self.create_documentation_directories(root_dir, package_name)
    package_root_dir = os.path.join(root_dir, package_name)
    (dependencies_map, resolved) = self.code_analyze_service.resolve_dependencies(package_root_dir)
    for symbol_info_str in resolved:
        dependencies = dependencies_map[symbol_info_str]
        self.symbol_documentation_generator_service.generate(root_dir, symbol_info_str, dependencies)
```

`generate_package_documentation`メソッドは、指定されたルートディレクトリとパッケージ名を受け取り、パッケージのドキュメントを生成するためのメソッドです。

このメソッドは、まず`create_documentation_directories`メソッドを呼び出して、ドキュメントのディレクトリ構造を作成します。次に、指定されたルートディレクトリとパッケージ名からパッケージのルートディレクトリのパスを取得します。

`code_analyze_service`を使用して、パッケージの依存関係を解析し、`dependencies_map`と`resolved`の2つの変数に結果を格納します。

`resolved`は、依存関係の解決済みのシンボル情報のリストです。このリストをループして、各シンボルに対して`dependencies_map`から依存関係を取得し、`symbol_documentation_generator_service`を使用してドキュメントを生成します。

## `DocumentationGeneratorService.generate_package_documentation`が依存関係にあるシンボルのドキュメント

依存する外部シンボルのドキュメントは以下の通りです。ただし、１つも存在しない場合もあります。

[シンボル1のドキュメント](シンボル1のドキュメントへのリンク)

[シンボル2のドキュメント](シンボル2のドキュメントへのリンク)

...

[シンボルNのドキュメント](シンボルNのドキュメントへのリンク)