# TODO: ハンドラを定義して，辞書`routes`に名前付きで登録してください。
# TODO: 現状，ハンドラはパラメータとして引数`params: list[str]`として受け取っていますが，変更を検討しても良いかもしれません。

from typing import Dict, Callable


def help(params: list[str]) -> None:
    print("Available commands:")
    print("- generate documentation: Generate documentation for a specific code file.")
    print("- optimize code: Provide code optimization suggestions.")
    print("- generate test cases: Generate test cases for a specific code file.")
    print("- help: Show available commands.")
    print("- exit: Exit the CLI.")


# TODO: implement
def exit(params: list[str]) -> None:
    print("Goodbye!")
    # cli = container.cli()
    # cli.running = False


def documentation(params: list[str]) -> None:
    print("Starting documentation generator...")
    while True:
        root_dir = input("Enter the dilectory to generate documentation for: ")
        package_name = input("Enter the python package name: ") # TODO: Pythonパッケージ専用の記述になってしまっているので注意！

        # TODO: バリデーションをもっと厳格に行うこと！
        if not (root_dir and package_name):
            print("Invalid input. Please try again.")
            continue
        
        # NOTE: トップレベルでインポートすると循環参照になるので，関数内で遅延インポートする。
        from documentationAI.container import container
        documentation_generator_service = container.documentation_generator_service()
        documentation_generator_service.generate_package_documentation(root_dir, package_name)
        break
    

def optimize_code(params: list[str]):
    # TODO: Implement the code to provide code optimization suggestions using the Documentation-AI system.
    print("Optimizing code...")


def generate_test_cases(params: list[str]):
    # TODO: Implement the code to generate test cases using the Documentation-AI system.
    print("Generating test cases...")


routes: Dict[str, Callable[[list[str]], None]] = {
    "help": help,
    "documentation": documentation,
    "optimize_code": optimize_code,
    "generate_test_cases": generate_test_cases,
    "exit": exit
}