# unit test for DependenciesAnalyzer

import documentationAI.domain.models.code_analyzer.python_limited.dependencies_analyzer as dependencies_analyzer


def test_analyze_dependencies():
    file_path = "/home/yama/Documents/Programming/documentation-AI/documentationAI/container.py"
    package_name = "documentationAI"
    analyzer = dependencies_analyzer.DependenciesAnalyzer(package_name)
    result = analyzer.analyze(file_path)
    for symbol_name, dependencies in result.items():
        print(symbol_name)
        for dependency in dependencies:
            print(f"\t{dependency.namespace}.{dependency.symbol_name}")

test_analyze_dependencies()
