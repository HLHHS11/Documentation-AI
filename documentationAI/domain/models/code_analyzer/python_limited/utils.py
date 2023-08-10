# FIXME: プロジェクトルートディレクトリ名とパッケージ名が同じ場合，正しいネームスペースが得られない！！！
import os

def filepath_to_namespace(filepath: str, package_name: str = "") -> str:
    # ファイルパスの/や\を.に置換し、.pyを削除する
    # if filepath.endswith('.py'):
    removed_py = filepath[:-3]
    
    namespace = removed_py.replace(os.sep, '.')

    # package_nameが指定されていた場合、ネームスペースをそのパッケージ名で始まるものに変換する
    if package_name:
        package_name_with_dot = package_name + '.'
        if package_name_with_dot in namespace:
            namespace = namespace[namespace.index(package_name_with_dot):]

    return namespace

# HACK: 絶対パスも得られるようになると便利そうなんだが…
def namespace_to_relativepath(namespace: str) -> str:
    return namespace.replace('.', os.sep) + '.py'