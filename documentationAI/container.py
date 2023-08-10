from dependency_injector import containers, providers

from documentationAI.interfaces.cli.cli import CLI
from documentationAI.interfaces.cli.router import Router
from documentationAI.interfaces.cli.handlers import routes
from documentationAI.domain.models.code_analyzer.python_limited.dependencies_analyzer import PythonDependenciesAnalyzer
from documentationAI.domain.models.code_analyzer.python_limited.code_analyzer import PythonCodeAnalyzer

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

    # PythonDependenciesAnalyerのコンストラクタ引数package_nameは，動的に指定される
    # コンテナの呼出側で，以下を実行することで得られる。
    # container.package_name.override("my_package")
    # analyzer = container.python_dependencies_analyzer()
    package_name = providers.Singleton(str)
    python_dependencies_analyzer = providers.Singleton(
        PythonDependenciesAnalyzer,
        package_name = package_name
    )

    python_code_analyzer = providers.Singleton(
        PythonCodeAnalyzer,
        dependencies_analyzer = python_dependencies_analyzer
    )


container = Container()
