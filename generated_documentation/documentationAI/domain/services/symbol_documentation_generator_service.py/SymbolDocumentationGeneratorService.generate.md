# `SymbolDocumentationGeneratorService.generate`のソース定義ファイル

```python
def generate(self, root_dir: str, symbol_info_str: str, dependencies: list[str]) -> None:
    file_path = self._get_file_path(symbol_info_str, root_dir)
    symbol_name = self._get_symbol_info(symbol_info_str).symbol_name
    symbol_definition = self.dependencies_analyzer.get_symbol_definition(file_path, symbol_name)
    dependency_docs: Dict[str, str] = {}
    for dependency_symbol_str in dependencies:
        print(f'dependency_symbol_str: {dependency_symbol_str}')
        dependency_path = self._calculate_doc_path(root_dir, dependency_symbol_str)
        dependency_doc = self._read_documentation(dependency_path)
        if dependency_doc:
            dependency_docs[dependency_symbol_str] = dependency_doc
    assembled_doc = self._assemble_documentation(symbol_name, symbol_definition, dependency_docs)
    preamble = f'あなたは優秀なソフトウェアエンジニアです。\n        以下に与えられるPythonのソースコードと周辺情報を読みながらドキュメント生成を行ってください。ただし，ドキュメントのスタイルは，MDN Web DocsのJavaScriptの解説ページのようなスタイルで，**マークダウン形式**で出力してください。\n        '
    prompt = '' + preamble + assembled_doc
    chat = ChatOpenAI(temperature=0.3)
    messages = [SystemMessage(content=preamble), HumanMessage(content=assembled_doc)]
    response = chat(messages)
    response_text = response.content
    print(response_text)
    save_path = self._calculate_doc_path(root_dir, symbol_info_str)
    with open(save_path, 'w') as file:
        file.write(response_text)
```

# `SymbolDocumentationGeneratorService.generate`が依存関係にあるシンボルのドキュメント

依存する外部シンボルのドキュメントは以下の通りである。ただし、１つも存在しない場合もあり得る。