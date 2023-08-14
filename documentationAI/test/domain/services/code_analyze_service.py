from documentationAI.container import container
from documentationAI.domain.services.package_analyze_service import PackageAnalyzeService


def code_analyze_service_test():
    container.package_name.override("documentationAI")  # type: ignore
    service: PackageAnalyzeService = container.package_analyze_service()
    package_root_dir = "/home/yama/Documents/Programming/documentation-AI/documentationAI"
    # package_name = "documentationAI"
    return service.resolve_dependencies(package_root_dir)


print(code_analyze_service_test())
