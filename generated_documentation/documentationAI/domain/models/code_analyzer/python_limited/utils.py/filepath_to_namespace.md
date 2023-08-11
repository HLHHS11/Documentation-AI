## `filepath_to_namespace`関数のドキュメント

`filepath_to_namespace`関数は、与えられたファイルパスをネームスペースに変換するための関数です。

### パラメータ

- `filepath` (str): 変換するファイルパス
- `package_name` (str, optional): パッケージ名。デフォルトは空文字列。

### 戻り値

- `namespace` (str): 変換されたネームスペース

### 例

```python
import os

def filepath_to_namespace(filepath: str, package_name: str='') -> str:
    removed_py = filepath[:-3]
    namespace = removed_py.replace(os.sep, '.')
    if package_name:
        package_name_with_dot = package_name + '.'
        if package_name_with_dot in namespace:
            namespace = namespace[namespace.index(package_name_with_dot):]
    return namespace

filepath = 'path/to/file.py'
package_name = 'my_package'

result = filepath_to_namespace(filepath, package_name)
print(result)  # 出力: my_package.to.file
```

### 依存関係

この関数は、以下の外部シンボルに依存しています。

- `os.sep`: ファイルパスのセパレータとして使用されます。