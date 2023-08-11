from documentationAI.domain.models.code_analyzer.python_limited.dependencies_analyzer import PythonDependenciesAnalyzer, python_symbol_parser
from documentationAI.domain.models.code_analyzer.python_limited.code_analyzer import PythonCodeAnalyzer

def test_python_code_analyzer():
    # NOTE: 以下のfilepathは，テスト実行環境に応じて変更する必要があります。本来はコード自体を環境に依存しないようにする必要がありますが…
    package_name = "documentationAI"
    package_root_dir = "/home/yama/Documents/Programming/documentation-AI/documentationAI"
    parser = python_symbol_parser
    code_analyzer = PythonCodeAnalyzer(PythonDependenciesAnalyzer(package_name, parser))
    dag = code_analyzer.generate_dag(package_root_dir)
    return dag

print(test_python_code_analyzer())