from typing import Any, Dict

from documentationAI.domain.models.document import Document
from documentationAI.domain.models.symbol import ISymbolId
from documentationAI.domain.services.prompt_generator.abc import IPromptGenerator, IPromptGeneratorContext


class DocumentationPromptGeneratorContext(IPromptGeneratorContext):

    def get_as_dict(self) -> Dict[str, Any]:
        return {
            "symbol_id": self.symbol_id,
            "symbol_def": self.symbol_def,
            "required_symbol_docs": self.required_symbol_docs,
        }
    
    def _set_by_dict(self, context_dict: Dict[str, Any]) -> None:
        symbol_id = context_dict["symbol_id"]
        symbol_def = context_dict["symbol_def"]
        required_symbol_docs = context_dict["required_symbol_docs"]
        # 非Noneチェック
        if not symbol_id:
            raise ValueError("symbol_id must be set")
        if not symbol_def:
            raise ValueError("symbol_def must be set")
        # required_symbol_docsが「空リスト以外の偽値」でないことをチェック
        if not required_symbol_docs and required_symbol_docs != []:
            raise ValueError("required_symbol_docs must be set")
        # 型チェック
        if not isinstance(symbol_id, ISymbolId):
            raise TypeError("symbol_id must be an instance of ISymbolId")
        if not isinstance(symbol_def, str):
            raise TypeError("symbol_def must be an instance of str")
        if not all(isinstance(doc, Document) for doc in required_symbol_docs):
            raise TypeError("all elements of required_symbol_docs must be an instance of Document")
        
        self.symbol_id = symbol_id
        self.symbol_def = symbol_def
        self.required_symbol_docs = required_symbol_docs

    @classmethod
    def from_dict(cls, context_dict: Dict[str, Any]) -> "DocumentationPromptGeneratorContext":
        context = cls()
        context._set_by_dict(context_dict)
        return context
    
    def get_symbol_id(self) -> ISymbolId:
        return self.symbol_id
    
    def get_symbol_def(self) -> str:
        return self.symbol_def
    
    def get_required_symbol_docs(self) -> list[Document]:
        return self.required_symbol_docs

# NOTE: ↓まだきちんと考察していないときに書いたのが以下のメモだが，テンプレートからプロンプトを生成する機能ぐらいならLangChainなしで作れる！しかも安全に！
class DocumentationPromptGenerator(IPromptGenerator):

    def __init__(self):
        # self._str_contexts: Dict[str, Any] = {}
        pass

    # TODO: 返り値を何らかの値オブジェクトでラップしたい
    # NOTE: 以下のtype:ignoreは，`context`の型は`IPromptGeneratorContext`にしなさい，と警告が出るため。
    #       おそらくこれは，ジェネリクスをうまく使えば解決できそうだが，現状は放置。
    def generate(self, context: DocumentationPromptGeneratorContext) -> str:  # type: ignore
        symbol_id = context.get_symbol_id()
        symbol_def = context.get_symbol_def()
        required_symbol_docs = context.get_required_symbol_docs()

        # TODO: "Python"の部分も動的に変更できるようにする
        preamble_template = f"""\
あなたは優秀なソフトウェアエンジニアであり，\
現在既存のPythonソフトウェア（パッケージ）のドキュメントを作成する作業を行っています。
今あなたが読んでいるのは，`{symbol_id.namespace}`というネームスペース上の`{symbol_id.symbol_name}`というシンボルです。\
このシンボルのドキュメントを，以下の注意点にしたがって作成してください。
- 与えられる情報は次の通り:
  このシンボルのソース定義，このシンボルが依存している，外部からインポートしてきたシンボルのドキュメント(依存関係がなければ存在しないこともある)
- 基本的には「シンボルのソース定義」を参考にして，そのシンボルの説明を考える。
  たとえば関数やクラスのメソッドであれば，その関数が何をするのか，引数は何を受け取るのか，戻り値は何を返すのか，などを考える。
  外部からインポートしてきたシンボル(依存先シンボル)の挙動がわかりにくい場合には，そのシンボルのドキュメントも参考にする。
変数やクラスそのものについては，それらのシンボルが何を表しているのかを考える
- 基本的には内部実装よりも，外部から見たときの振る舞いがわかりやすいように説明する。
  内部実装については，最後の章の`# 内部実装について`で説明する。
- ドキュメントのスタイルは，MDN Web DocsのJavaScriptの解説ページのようなスタイルで，**マークダウン形式**で出力すること。\
具体的な形式は，以下を参考にしてください。
``` markdown:example.md
# {{シンボル名(例: Array.prototype.filter()}}
{{シンボルに対する短く完結な説明文(例:`filter()`メソッドは，この配列の中から，提供された関数で実装されたテストに合格した要素のみを抽出したシャローコピーを作成します。)}}

# 構文
``` {{言語名(例:js)}}
{{関数やメソッドの場合，どのように値を代入するかサンプルを書く}}
```
# 引数
{{引数の説明を箇条書きする。引数がなければ"引数はありません。"と表示する。１行目に引数シンボル名，２行目に概要を説明する。(例:
- `callbackFn`  
  配列の各要素に対して実行するテスト関数です。この関数が`true`を返した要素は残され，`false`を返した要素は取り除かれます。  
  この関数は以下の引数と共に呼び出されます。
  - `element`  
    配列内で処理中の現在の要素です。
  - `index`  
    配列内で処理中の現在の要素の位置です。
  - `array`  
    `filter()`が呼び出された配列です。)}}
# 返値
{{返り値の説明を書く。返り値の型についても言及すること。返り値がない場合には"返り値: void"や"返り値: None"などと表示する}}

# 解説
{{シンボルの詳しい解説を書く。ある程度は自由に書いてよい。詳細な振る舞いについての説明でも，\
例としてシンボルのユースケースを書く，でもよい。}}

# 内部実装について
{{ここでは，シンボルを使う側(外部)ではなく，シンボルに変更を加える際などに参考にするべき情報が書かれる。\
内部実装の処理フローや，内部で利用しているデータ構造などを説明する。}}
```
"""

        assembled_required_symbol_docs = self._assemble_required_symbol_docs(symbol_id, required_symbol_docs)

        prompt = f"""
{preamble_template}

---

それでは，実際のソース定義および依存しているシンボルのドキュメントを以下に示します。

# `{symbol_id.symbol_name}`のソース定義
``` python
{symbol_def}
```

# `{symbol_id.symbol_name}`が依存関係にあるシンボルのドキュメント
{assembled_required_symbol_docs}

"""

        return prompt
    

    def _assemble_required_symbol_docs(self, symbol_id: ISymbolId, required_symbol_docs: list[Document]) -> str:
        if len(required_symbol_docs) == 0:
            return f"{symbol_id.symbol_name}は，他のシンボルに依存していません。"
        
        assembled_doc = f"""\
{symbol_id.symbol_name}は，以下のシンボルに依存しています。
"""
        
        for doc in required_symbol_docs:
            assembled_doc += f"""\
## `{doc.get_symbol_id().stringify}`のドキュメント
``` markdown
{doc.get_content()}
```
"""
        return assembled_doc
