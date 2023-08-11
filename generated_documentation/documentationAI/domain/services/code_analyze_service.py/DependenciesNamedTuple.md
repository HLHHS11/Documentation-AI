## DependenciesNamedTuple

`DependenciesNamedTuple`は、依存関係を表すための名前付きタプルです。

### プロパティ

- `dependencies` (`Dict[str, list[str]]`): キーがシンボル名、値がそのシンボルが依存しているシンボルのリストです。
- `resolved` (`list[str]`): 解決済みの依存関係のシンボルのリストです。

### 使用例

```python
from typing import Dict, List, NamedTuple

class DependenciesNamedTuple(NamedTuple):
    dependencies: Dict[str, List[str]]
    resolved: List[str]

# 依存関係を持つDependenciesNamedTupleのインスタンスを作成する
dependencies = {
    'A': ['B', 'C'],
    'B': ['C'],
    'C': []
}
resolved = ['C', 'B', 'A']
dependency_tuple = DependenciesNamedTuple(dependencies, resolved)

# インスタンスのプロパティにアクセスする
print(dependency_tuple.dependencies)  # {'A': ['B', 'C'], 'B': ['C'], 'C': []}
print(dependency_tuple.resolved)  # ['C', 'B', 'A']
```

### 依存する外部シンボルのドキュメント

依存する外部シンボルのドキュメントは以下の通りである。ただし、１つも存在しない場合もあり得る。