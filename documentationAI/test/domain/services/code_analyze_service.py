# NOTE: ここに書くべきテストではないかも！？しかも他のテストコードに依存してるし…
# dagを取得してトポロジカルソートするサンプルコード

from documentationAI.utils.topological_sort import topological_sort
from documentationAI.domain.models.code_analyzer.python_limited.code_analyzer import PythonCodeAnalyzer
from documentationAI.domain.models.code_analyzer.python_limited.dependencies_analyzer import PythonDependenciesAnalyzer

def test_analysis_sort():
    # NOTE: 以下のfilepathは，テスト実行環境に応じて変更する必要があります。本来はコード自体を環境に依存しないようにする必要がありますが…
    package_name = "documentationAI"
    package_root_dir = "/home/yama/Documents/Programming/documentation-AI/documentationAI"
    code_analyzer = PythonCodeAnalyzer(PythonDependenciesAnalyzer(package_name))
    dag = code_analyzer.generate_dag(package_root_dir)
    return topological_sort(dag)

result = test_analysis_sort()
for symbol_info in result:
    print(symbol_info)