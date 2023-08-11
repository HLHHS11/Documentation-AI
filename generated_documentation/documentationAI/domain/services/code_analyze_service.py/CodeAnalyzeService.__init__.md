# CodeAnalyzeService.__init__

`CodeAnalyzeService.__init__`メソッドは、`code_analyzer`と`parser`という2つの引数を受け取ります。このメソッドは、`code_analyzer`と`parser`をインスタンス変数として保持します。

## ソース定義ファイル

```python
def __init__(self, code_analyzer: ICodeAnalyzer, parser: Callable[[list[str], str], ISymbolInfo | str]) -> None:
    self.code_analyzer = code_analyzer
    self.parser = parser
```

## 依存する外部シンボルのドキュメント

`CodeAnalyzeService.__init__`メソッドは、以下の外部シンボルに依存しています。

### documentationAI.domain.models.code_analyzer.abc:ICodeAnalyzer

`ICodeAnalyzer`は、`CodeAnalyzeService`のコンストラクタに渡される`code_analyzer`引数の型です。

#### ソース定義ファイル

```python
class ICodeAnalyzer(abc.ABC):

    def __init__(self, dependencies_analyzer: IDependenciesAnalyzer):
        self.dependencies_analyzer = dependencies_analyzer

    @abc.abstractmethod
    def generate_dag(self, package_root_dir: str) -> Dict[str, list[str]]:
        pass

    @abc.abstractmethod
    def parse_symbol_str(self, symbol_str: str) -> ISymbolInfo:
        pass
```

#### 依存する外部シンボルのドキュメント

`ICodeAnalyzer`は、以下の外部シンボルに依存しています。

##### documentationAI.domain.models.code_analyzer.abc:IDependenciesAnalyzer

`IDependenciesAnalyzer`は、`ICodeAnalyzer`のコンストラクタに渡される`dependencies_analyzer`引数の型です。

##### 依存する外部シンボルのドキュメント

依存する外部シンボルのドキュメントはありません。

### documentationAI.domain.models.code_analyzer.abc:ISymbolInfo

`ISymbolInfo`は、`CodeAnalyzeService`のコンストラクタに渡される`parser`引数の型です。

#### ソース定義ファイル

```python
class ISymbolInfo(abc.ABC):

    @property
    @abc.abstractmethod
    def namespace(self) -> str:
        pass

    @property
    @abc.abstractmethod
    def symbol_name(self) -> str:
        pass

    @abc.abstractmethod
    def stringify(self) -> str:
        pass

    @classmethod
    @abc.abstractmethod
    def parse(cls, stringified: str) -> ISymbolInfo:
        pass
```

#### 依存する外部シンボルのドキュメント

`ISymbolInfo`は、以下の外部シンボルに依存しています。

##### 依存する外部シンボルのドキュメント

依存する外部シンボルのドキュメントはありません。