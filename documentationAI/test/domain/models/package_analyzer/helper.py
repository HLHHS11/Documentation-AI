# unit test for PythonAnalyzerHelper
from documentationAI.domain.models.package_analyzer.python_limited.helper import PythonAnalyzerHelper

def test_parse_symbol_str():
    pass

def test_abspath_to_namespace():
    helper = PythonAnalyzerHelper()
    assert helper.abspath_to_namespace(
        "/home/yama/Documents/Programming/documentation-AI/documentationAI/domain/models/package_analyzer/python_limited/package_analyzer.py", "documentationAI"
    ) == "documentationAI.domain.models.package_analyzer.python_limited.package_analyzer"

def test_namespace_to_abspath():
    helper = PythonAnalyzerHelper()
    assert helper.namespace_to_abspath(
        "documentationAI.domain.models.package_analyzer.python_limited.package_analyzer", "/home/yama/Documents/Programming/documentation-AI/documentationAI"
    ) == "/home/yama/Documents/Programming/documentation-AI/documentationAI/domain/models/package_analyzer/python_limited/package_analyzer.py"


test_abspath_to_namespace()