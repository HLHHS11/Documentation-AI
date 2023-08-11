# `CodeAnalyzeService.resolve_dependencies`のソース定義

```python
def resolve_dependencies(self, package_root_dir: str) -> DependenciesNamedTuple:
    dependencies_map = self.code_analyzer.generate_dag(package_root_dir)
    resolved = topological_sort(dependencies_map)
    return DependenciesNamedTuple(dependencies_map, resolved)
```

`CodeAnalyzeService.resolve_dependencies`は、与えられたパッケージのルートディレクトリを基に依存関係を解決するためのメソッドです。このメソッドは、`package_root_dir`を引数として受け取り、`DependenciesNamedTuple`を返します。

このメソッドでは、`self.code_analyzer.generate_dag`メソッドを使用して依存関係のマップを生成し、`topological_sort`関数を使用してトポロジカルソートされた依存関係を取得します。最終的に、`DependenciesNamedTuple`を作成して、依存関係のマップとトポロジカルソートされた結果を返します。

# `CodeAnalyzeService.resolve_dependencies`が依存する外部シンボルのドキュメント

## `topological_sort`関数

`topological_sort`関数は、与えられた有向非巡回グラフ（DAG）をトポロジカルソートするための関数です。

### パラメータ

- `dag`（`dict[str, list[str]]`）: トポロジカルソートを行う対象のグラフ。キーはノードの名前を表し、値はそのノードが依存しているノードのリストです。

### 戻り値

- `list[str]`: トポロジカルソートされたノードのリスト。

### 使用例

```python
dag = {
    'A': ['B', 'C'],
    'B': ['D'],
    'C': ['D'],
    'D': []
}

sorted_nodes = topological_sort(dag)
print(sorted_nodes)  # ['A', 'C', 'B', 'D']
```

この関数は、外部のシンボルには依存していません。