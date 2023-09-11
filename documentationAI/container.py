from dependency_injector import containers, providers

from documentationAI.interfaces.cli.cli import CLI
from documentationAI.interfaces.cli.router import Router
from documentationAI.interfaces.cli.handlers import routes
from documentationAI.domain.models.package_analyzer.python_limited.module_analyzer import PythonModuleAnalyzer
from documentationAI.domain.models.package_analyzer.python_limited.package_analyzer import PythonPackageAnalyzer
from documentationAI.application.documentation_service import DocumentationService
from documentationAI.domain.services.package_analyze_service import PackageAnalyzeService
from documentationAI.domain.services.symbol_documentation_service import SymbolDocumentationService
from documentationAI.domain.models.package_analyzer.python_limited.helper import PythonAnalyzerHelper


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
    
    package_analyze_service = providers.Factory(
        PackageAnalyzeService,
        package_analyzer = package_analyzer,
        helper = helper
    )

    symbol_documentation_service = providers.Factory(
        SymbolDocumentationService,
        module_analyzer = module_analyzer,
        helper = helper
    )

    documentation_service = providers.Singleton(
        DocumentationService,
        package_analyze_service = package_analyze_service,
        symbol_documentation_service = symbol_documentation_service
    )


container = Container()
