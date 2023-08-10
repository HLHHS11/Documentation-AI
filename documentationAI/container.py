from dependency_injector import containers, providers

from documentationAI.interfaces.cli.cli import CLI
from documentationAI.interfaces.cli.router import Router
from documentationAI.interfaces.cli.handlers import routes
from documentationAI.domain.models.code_analyzer.python_limited.dependencies_analyzer import PythonDependenciesAnalyzer
from documentationAI.domain.models.code_analyzer.python_limited.code_analyzer import PythonCodeAnalyzer
from documentationAI.application.documentation_generator import DocumentationGeneratorService
from documentationAI.domain.services.code_analyze_service import CodeAnalyzeService



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

    @staticmethod
    def _package_name_undefined_error() -> str:
        raise ValueError("package_name must be specified by overriding.")
    
    # NOTE: オーバーライド必須
    package_name = providers.Callable(_package_name_undefined_error)
    
    dependencies_analyzer = providers.Singleton(
        PythonDependenciesAnalyzer, # TODO: 抽象クラスによるバインドを行いたい。いずれ多言語対応する際に，コード解析器を動的に切り替えられるようにする必要あり。
        package_name = package_name
    )

    code_analyzer = providers.Singleton(
        PythonCodeAnalyzer, # TODO: 抽象クラスによるバインドを行いたい。いずれ多言語対応する際に，コード解析器を動的に切り替えられるようにする必要あり。
        dependencies_analyzer = dependencies_analyzer
    )
    
    code_analyze_service = providers.Singleton(
        CodeAnalyzeService,
        code_analyzer = code_analyzer
    )

    documentation_generator_service = providers.Singleton(
        DocumentationGeneratorService,
        code_analyze_service = code_analyze_service
    )


container = Container()
