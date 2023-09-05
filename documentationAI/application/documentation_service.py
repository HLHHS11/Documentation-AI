import os

from documentationAI.domain.services.package_analyze_service import PackageAnalyzeService
from documentationAI.domain.services.symbol_documentation_service import SymbolDocumentationService

class DocumentationService:

    def __init__(
            self,
            package_analyze_service: PackageAnalyzeService,   # NOTE: 抽象クラス`ICodeAnalyzer`を受け取る必要はない
            symbol_documentation_service: SymbolDocumentationService
    ):
        self.package_analyze_service = package_analyze_service
        self.symbol_documentation_service = symbol_documentation_service
    

    def generate_package_documentation(
        self,
        project_root_dir: str,
        package_root_dir: str,
        package_name: str
    ) -> None:

        # TODO: リポジトリで代替する
        self.create_documentation_directories(project_root_dir, package_name)
        
        # パッケージ解析サービスを利用して，シンボルの依存関係と解決順序を取得
        dependencies_map, resolved = self.package_analyze_service.resolve_dependencies(package_root_dir, package_name)
        
        # TODO: implement. 解決された順番にしたがってドキュメンテーション生成を行う。
        for symbol_info_str in resolved:
            # NOTE: symbol_infoのパースは，symbol_documentation_generator_service.generate()内で行うことにする！！！
            dependencies = dependencies_map[symbol_info_str]
            # NOTE: 今回は，symbol_info_strにパッケージ名の情報が含まれているので，`rood_dir`の方が`package_root_dir`より適切。
            self.symbol_documentation_service.generate(project_root_dir, symbol_info_str, dependencies)
    

    def create_documentation_directories(self, root_dir: str, package_name: str) -> None:
        package_root_dir = os.path.join(root_dir, package_name)
        documentation_root_dir = os.path.join(root_dir, "generated_documentation", package_name)
        self._create_directory_structure(package_root_dir, documentation_root_dir)
    
    def _create_directory_structure(self, source_dir: str, target_dir: str) -> None:
        os.makedirs(target_dir, exist_ok=True)
        for item in os.listdir(source_dir):
            if item == "__pycache__":
                continue    # __pycache__は無視
            source_path = os.path.join(source_dir, item)
            target_path = os.path.join(target_dir, item)
            if os.path.isdir(source_path):
                self._create_directory_structure(source_path, target_path)
            elif os.path.isfile(source_path) and item.endswith('.py'):
                os.makedirs(os.path.join(target_path), exist_ok=True)