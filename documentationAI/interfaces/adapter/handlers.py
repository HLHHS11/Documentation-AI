# TODO: ハンドラを定義して，辞書`routes`に名前付きで登録してください。
# TODO: 現状，ハンドラはパラメータとして引数`params: list[str]`として受け取っていますが，変更を検討しても良いかもしれません。
import os
import asyncio
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



def documentation(params: list[str]) -> None:
    print("Starting documentation generator...")
    while True:
        project_root_dir = input("Enter the absolute dilectory path to generate documentation for:\n\t")   # TODO: 相対パスによる記述等にも対応すること！(documentation_generator_service等の改修も必要になるだろう。)
        if not os.path.exists(project_root_dir):
            print("[Error]: The specified directory does not exist. Please try again. (Hint: use absolute path)")
            continue
        package_root_dir = input("Enter the absolute dilectory path to the package to generate documentation for:\n\t")   # TODO: 相対パスによる記述等にも対応すること！(documentation_generator_service等の改修も必要になるだろう。)
        if not os.path.exists(package_root_dir):
            print("[Error]: The specified package directory does not exist. Please try again.")
            continue
        package_name = input("Enter the python package name:\n\t") # TODO: Pythonパッケージ専用の記述になってしまっているので注意！
        
        # NOTE: トップレベルでインポートすると循環参照になるので，関数内で遅延インポートする。
        from documentationAI.container import container
        container.config.from_dict({    # TODO: ここでifもつけずに設定するのはかなり強引。後で修正すること。
            "local_directory": {
                "project_root_dir": project_root_dir,
                "package_root_dir": package_root_dir,
                "package_name": package_name
            },
            "sqlite": {
                "db_path": os.path.join(project_root_dir, "docai_db.sqlite")
            }
        })
        documentation_service = container.documentation_service()

        asyncio.run(documentation_service.generate_package_documentation(project_root_dir, package_root_dir, package_name))
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
