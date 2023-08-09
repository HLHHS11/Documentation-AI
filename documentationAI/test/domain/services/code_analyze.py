# NOTE: ここに書くべきテストではないかも！？しかも他のテストコードに依存してるし…
# dagを取得してトポロジカルソートするサンプルコード

from documentationAI.test.domain.models.code_analyzer.python_limited.code_analyzer import test_python_code_analyzer
from documentationAI.utils.topological_sort import topological_sort

def test_analysis_sort():
    dag = test_python_code_analyzer()
    return topological_sort(dag)

result = test_analysis_sort()
for symbol_info in result:
    print(symbol_info)