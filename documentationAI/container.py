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
    """_summary_
    [重要]: `package_name`の指定（オーバーライド）を行わずに，`package_name`に依存するオブジェクトを呼び出すとエラーが発生します。
    必ず呼出側で`package_name`をオーバーライドしてください。例:
    ``` python
        container.package_name.override("my_package")
        analyzer = container.python_dependencies_analyzer()
    ```
    Args:
        containers (_type_): _description_

    Raises:
        ValueError: _description_
    """    

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

    # PythonDependenciesAnalyerのコンストラクタ引数package_nameは，動的に指定される
    # コンテナの呼出側で，以下のようにpackage_nameをオーバーライドすることで得られる。
    # container.package_name.override("my_package")
    # analyzer = container.python_dependencies_analyzer()

    # @staticmethod
    # def _package_name_undefined_error() -> str:
    #     raise ValueError("package_name must be specified by overriding.")
    
    # # NOTE: オーバーライド必須
    # package_name = providers.Callable(_package_name_undefined_error)

    helper = providers.Factory(
        PythonAnalyzerHelper
    )
    
    module_analyzer = providers.Factory(
        PythonModuleAnalyzer, # TODO: 抽象クラスによるバインドを行いたい。いずれ多言語対応する際に，コード解析器を動的に切り替えられるようにする必要あり。
        # package_name = package_name,
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
        package_analyze_service = package_analyze_service,
        module_analyzer = module_analyzer,
        helper = helper
    )

    documentation_service = providers.Singleton(
        DocumentationService,
        package_analyze_service = package_analyze_service,
        symbol_documentation_service = symbol_documentation_service
    )


container = Container()
