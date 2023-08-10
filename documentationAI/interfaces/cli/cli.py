# from typing import Callable

from documentationAI.interfaces.cli.router import Router


class CLI:

    def __init__(self, router: Router) -> None:
        self.router = router
        self.running = True
        # HACK: "exit"専用にハンドラを登録しているが，絶対に良くないので修正したい。
        self.router.register("exit", self._exit)

    def run(self) -> None:
        print("Welcome to Documentation-AI!")
        print("Type 'help' for available commands or 'exit' to quit.")

        while self.running:
            command = input(">> ")
            self.handle(command)
    

    def handle(self, request: str) -> None:
        # NOTE: 現時点ではコマンドパラメータを扱うことはないが，必要に応じてコマンドパラメータのパースも行うようにすること。
        self.router.handle(request, [])


    def _exit(self, params: list[str]) -> None:
        print("Goodbye!")
        self.running = False
