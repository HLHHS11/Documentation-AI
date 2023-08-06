from dependency_injector import containers, providers

from documentationAI.interfaces.cli import CLI
from documentationAI.interfaces.router import Router
from documentationAI.interfaces.handlers import routes


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


container = Container()

