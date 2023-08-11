from documentationAI.container import container
from documentationAI.application.documentation_generator import DocumentationGeneratorService


def documentation_generator_service_test():
    container.package_name.override("documentationAI")  # type: ignore
    application_service: DocumentationGeneratorService = container.documentation_generator_service()
    root_dir = "/home/yama/Documents/Programming/documentation-AI"
    package_name = "documentationAI"
    application_service.generate_package_documentation(root_dir, package_name)


documentation_generator_service_test()
