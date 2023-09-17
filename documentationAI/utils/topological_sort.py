from graphlib import TopologicalSorter
from typing import TypeVar

T = TypeVar('T')

def topological_sort(dag: dict[T, list[T]]) -> list[T]:
    ts = TopologicalSorter(dag)
    return list(ts.static_order())
