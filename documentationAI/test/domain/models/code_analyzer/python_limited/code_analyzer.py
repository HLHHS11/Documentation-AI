from documentationAI.domain.models.package_analyzer.python_limited.module_analyzer import PythonModuleAnalyzer
from documentationAI.domain.models.package_analyzer.python_limited.package_analyzer import PythonPackageAnalyzer
# import helper class for python
from documentationAI.domain.models.package_analyzer.python_limited.helper import PythonAnalyzerHelper

def test_python_package_analyzer():
    # NOTE: 以下のfilepathは，テスト実行環境に応じて変更する必要があります。本来はコード自体を環境に依存しないようにする必要がありますが…
    package_name = "documentationAI"
    package_root_dir = "/home/yama/Documents/Programming/documentation-AI/documentationAI"
    helper = PythonAnalyzerHelper()
    package_analyzer = PythonPackageAnalyzer(PythonModuleAnalyzer(package_name, helper), helper)
    dag = package_analyzer.generate_dag(package_root_dir)
    return dag

print(test_python_package_analyzer())