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

## 依存する外部シンボルのドキュメント

この関数は、外部のシンボルには依存していません。