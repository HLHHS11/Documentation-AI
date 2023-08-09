from graphlib import TopologicalSorter

def topological_sorter(dag: dict[str, list[str]]) -> list[str]:
    ts = TopologicalSorter(dag)
    return list(ts.static_order())
