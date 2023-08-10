import os

from documentationAI.domain.services.code_analyze_service import CodeAnalyzeService


class DocumentationGeneratorService:

    def __init__(
            self,
            code_analyze_service: CodeAnalyzeService,   # NOTE: 抽象クラス`ICodeAnalyzer`を受け取る必要はない
    ):
        self.code_analyze_service = code_analyze_service
    

    def generate_package_documentation(self, root_dir: str, package_name: str) -> None:
        
        package_root_dir = os.path.join(root_dir, package_name)

        # dependencies, resolved = self.code_analyze_service.resolve_dependencies(package_root_dir)
        dependencies, resolved = self.code_analyze_service.resolve_dependencies(package_root_dir)
        
        # TODO: implement. 解決された順番にしたがってドキュメンテーション生成を行う。
        # リストresolvedを逆順で処理する
        for symbol_info_str in reversed(resolved):
            # symbol_info_strをPythonSymbolInfoに変換
            symbol_info = self.code_analyze_service.parse_symbol_str(symbol_info_str)
            print(symbol_info)
            # symbol_infoに対応するファイルのドキュメンテーションを生成
            # self.generate_documentation_for_symbol(symbol_info, package_root_dir)