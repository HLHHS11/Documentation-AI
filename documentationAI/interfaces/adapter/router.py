from typing import Callable, Dict


class Router:
    def __init__(self, routes: Dict[str, Callable[[list[str]], None]]):
        self.routes = routes

    def register(self, request: str, callback: Callable[[list[str]], None]) -> None:
        self.routes[request] = callback
    
    def handle(self, request: str, params: list[str]) -> None:
        if request in self.routes:
            handler = self.routes[request]
            handler(params)
        else:
            print("Invalid command. Type 'help' for available commands.")
