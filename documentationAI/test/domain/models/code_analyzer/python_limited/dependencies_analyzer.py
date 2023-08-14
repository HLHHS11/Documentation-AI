# unit test for DependenciesAnalyzer

import documentationAI.domain.models.package_analyzer.python_limited.module_analyzer as module_analyzer


def test_analyze_dependencies():
    # NOTE: 以下のfilepathは，テスト実行環境に応じて変更する必要があります。本来はコード自体を環境に依存しないようにする必要がありますが…
    file_path = "/home/yama/Documents/Programming/documentation-AI/documentationAI/domain/models/package_analyzer/python_limited/dependencies_analyzer.py"
    package_name = "documentationAI"
    parser = module_analyzer.python_symbol_parser
    analyzer = module_analyzer.PythonModuleAnalyzer(package_name, parser)
    namespace, result = analyzer.analyze(file_path)
    print(f"==={namespace}===")
    for symbol_name, dependencies in result.items():
        print(symbol_name)
        for dependency in dependencies:
            print(f"\t{dependency.namespace}.{dependency.symbol_name}")
    
test_analyze_dependencies()

print("=========")

def test_get_symbol_definition():
    # file_path = "/home/yama/Documents/Programming/documentation-AI/documentationAI/domain/models/package_analyzer/python_limited/dependencies_analyzer.py"
    file_path = "/home/yama/Documents/Programming/documentation-AI/documentationAI/container.py"
    package_name = "documentationAI"
    parser = module_analyzer.python_symbol_parser
    analyzer = module_analyzer.PythonModuleAnalyzer(package_name, parser)
    # symbol_definition = analyzer.get_symbol_definition(file_path, "PythonDependenciesAnalyzer.analyze")
    symbol_definition = analyzer.get_symbol_impl(file_path, "container.dependencies_analyzer")
    return symbol_definition

print(test_get_symbol_definition())
