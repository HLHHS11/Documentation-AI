# from typing import Callable

from documentationAI.interfaces.router import Router
# from documentationAI.interfaces.handlers import Handlers


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
    

    # def register(self, request: str, callback: Callable[[list[str]], None]) -> None:
    #     self.router.register(request, callback)
    

    def handle(self, request: str) -> None:
        self.router.handle(request, [])


    def _exit(self, params: list[str]) -> None:
        print("Goodbye!")
        self.running = False
    

    # def handle_command(self, command: str) -> None:
    #     if command.lower() == "exit":
    #         print("Goodbye!")
    #         self.running = False
    #     elif command.lower() == "help":
    #         self.show_help()
    #     elif command.lower() == "generate documentation":
    #         self.generate_documentation()
    #     elif command.lower() == "optimize code":
    #         self.optimize_code()
    #     elif command.lower() == "generate test cases":
    #         self.generate_test_cases()
    #     else:
    #         print("Invalid command. Type 'help' for available commands.")

    # def show_help(self) -> None:
    #     print("Available commands:")
    #     print("- generate documentation: Generate documentation for a specific code file.")
    #     print("- optimize code: Provide code optimization suggestions.")
    #     print("- generate test cases: Generate test cases for a specific code file.")
    #     print("- help: Show available commands.")
    #     print("- exit: Exit the CLI.")

    # def generate_documentation(self) -> None:
    #     # TODO: Implement the code to generate documentation using the Documentation-AI system.
    #     print("Generating documentation...")

    # def optimize_code(self):
    #     # TODO: Implement the code to provide code optimization suggestions using the Documentation-AI system.
    #     print("Optimizing code...")

    # def generate_test_cases(self):
    #     # TODO: Implement the code to generate test cases using the Documentation-AI system.
    #     print("Generating test cases...")




# DIコンテナ使用のため，main()は不要になった
# def main() -> None:
#     cli = CLI()
#     cli.run()

# if __name__ == "__main__":
#     main()
