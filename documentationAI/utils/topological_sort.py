from typing import Dict

# 引数の例:
# graph = {
#     # A->B,C; B->E; C->E,F; D->C,E; E->null; F->E; G->F
#     'A': ['B', 'C'],
#     'B': ['E'],
#     'C': ['E', 'F'],
#     'D': ['C', 'E'],
#     'E': [],
#     'F': ['E'],
#     'G': ['F']
# }
# 各シンボルの依存関係解決においては，キーを`名前空間名前.シンボル名`のように登録し，値を依存するシンボル(キーと同様の名前)のリストとする。
def topological_sort(graph: Dict[str, list[str]]):
    # 入次数を計算
    in_degree = {node: 0 for node in graph}
    for node in graph:
        for neighbor in graph[node]:
            in_degree[neighbor] += 1
    
    # 入次数が0のノードをキューに追加
    queue: list[str] = []
    for node in graph:
        if in_degree[node] == 0:
            queue.append(node)
    
    # ソート結果を格納するリスト
    sorted_order: list[str] = []

    # キューからノードを取り出しながら処理
    while queue:
        # 入次数が0のノードを1つ取り出す
        node = queue.pop(0)
        sorted_order.append(node)

        # 取り出したノードに隣接するノードの入次数を1減らす
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1

            # 入次数が0になったらキューに追加
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    
    return sorted_order
