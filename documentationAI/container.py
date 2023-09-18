from dependency_injector import containers, providers
from documentationAI.domain.services.prompt_generator.documentation import DocumentationPromptGenerator

from documentationAI.interfaces.adapter.cli import CLI
from documentationAI.interfaces.adapter.router import Router
from documentationAI.interfaces.adapter.handlers import routes
from documentationAI.domain.implementation.python.module_analyzer import PythonModuleAnalyzer
from documentationAI.domain.implementation.python.package_analyzer import PythonPackageAnalyzer
from documentationAI.application.documentation_service import DocumentationService
from documentationAI.domain.implementation.python.helper import PythonAnalyzerHelper
from documentationAI.interfaces.repository.document_repository_impl.in_memory import InMemoryDocumentRepositoryImpl
from documentationAI.interfaces.repository.document_repository_impl.sqlite import SQLiteDocumentRepositoryImpl


class Container(containers.DeclarativeContainer):

    # TODO: 現状，configは必要ないのだが…
    config = providers.Configuration()

    routes = providers.Dict(routes)

    router = providers.Singleton(
        Router,
        routes = routes
    )

    cli = providers.Singleton(
        CLI,
        router = router
    )

    helper = providers.Factory(
        PythonAnalyzerHelper
    )
    
    module_analyzer = providers.Factory(
        PythonModuleAnalyzer, # TODO: 抽象クラスによるバインドを行いたい。いずれ多言語対応する際に，コード解析器を動的に切り替えられるようにする必要あり。
        helper = helper
    )

    package_analyzer = providers.Factory(
        PythonPackageAnalyzer, # TODO: 抽象クラスによるバインドを行いたい。いずれ多言語対応する際に，コード解析器を動的に切り替えられるようにする必要あり。
        module_analyzer = module_analyzer,
        helper = helper
    )

    # document_repository = providers.Singleton(
    #     SQLiteDocumentRepositoryImpl,
    #     sqlite_db_path = config.sqlite.db_path
    # )

    document_repository = providers.Singleton(
        InMemoryDocumentRepositoryImpl,
    )

    prompt_generator = providers.Factory(
        DocumentationPromptGenerator,
    )

    documentation_service = providers.Factory(
        DocumentationService,
        package_analyzer = package_analyzer,
        document_repository = document_repository,
        helper = helper,
        prompt_generator = prompt_generator
    )


container = Container()
