# `python_symbol_parser`のソース定義ファイル

```python
def python_symbol_parser(args: list[str], mode: str) -> PythonSymbolInfo | str:
    """_summary_
    `GetSymbolInfo`モード: 引数の文字列を`PythonSymbolInfo`に変換して返します。`args[0] = symbol_str = <namespace>:<symbol_name>`の形式  
    `GetFilePath`モード: 引数の文字列からファイルパスを取得して返します。`args[0] = symbol_str = <namespace>:<symbol_name>, args[1] = <root_dir_path>`の形式
    Args:
        args (list[str]): 引数の文字列のリスト
        mode (str): モードを指定する文字列

    Returns:
        PythonSymbolInfo|str: _description_
    """
    if mode == 'GetSymbolInfo':
        symbol_str = args[0]
        return PythonSymbolInfo.parse(symbol_str)
    elif mode == 'GetFilePath':
        symbol_str = args[0]
        root_dir_path = args[1]
        (namespace, _) = symbol_str.split(':')
        return os.path.join(root_dir_path, namespace.replace('.', os.sep) + '.py')
    else:
        raise ValueError(f'Invalid mode: {mode}')
```

# 依存する外部シンボルのドキュメント

依存する外部シンボルのドキュメントは以下の通りである。ただし、１つも存在しない場合もあり得る。