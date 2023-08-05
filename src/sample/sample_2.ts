/**
 * @file インポートしている関数・クラスのソース定義を取得するサンプル
 */

import ts from 'typescript';
import * as fs from 'fs';
import * as path from 'path';

const options: ts.CompilerOptions = {
  target: ts.ScriptTarget.ESNext,
  module: ts.ModuleKind.ESNext,
};

function parseSourceFile(filePath: string): ts.SourceFile {
  const code = fs.readFileSync(filePath, 'utf-8');
  return ts.createSourceFile(filePath, code, ts.ScriptTarget.ESNext, true);
}

function getImports(sourceFile: ts.SourceFile, resolver: ts.ModuleResolutionCache): string[] {
  const imports: string[] = [];
  ts.forEachChild(sourceFile, (node) => {
    if (ts.isImportDeclaration(node)) {
      const moduleSpecifier = node.moduleSpecifier as ts.StringLiteral;
      const host = ts.createCompilerHost(options);
      const resolvedModule = ts.resolveModuleName(moduleSpecifier.text, sourceFile.fileName, options, host, resolver);
      if (resolvedModule && resolvedModule.resolvedModule) {
        const importPath = resolvedModule.resolvedModule.resolvedFileName;
        imports.push(importPath);
      }
    }
  });
  return imports;
}

function getDefinitionText(sourceFilePath: string, symbolName: string): string | null {
  const sourceFile = parseSourceFile(sourceFilePath);
  let definitionText: string | null = null;

  ts.forEachChild(sourceFile, (node) => {
    if (ts.isFunctionDeclaration(node) && node.name && node.name.text === symbolName) {
      definitionText = node.getText(sourceFile);
    } else if (ts.isClassDeclaration(node) && node.name && node.name.text === symbolName) {
      definitionText = node.getText(sourceFile);
    }
  });

  return definitionText;
}

function main() {
  const mainFilePath = '/path/to/your/main/file.ts';
  const mainSourceFile = parseSourceFile(mainFilePath);
  const resolver = ts.createModuleResolutionCache(path.dirname(mainFilePath), (x) => x);
  const imports = getImports(mainSourceFile, resolver);

  // インポートされているファイルのシンボルの定義部分のテキストを表示
  for (const importedFilePath of imports) {
    const importedFileName = path.basename(importedFilePath, '.js');
    const definitionText = getDefinitionText(importedFilePath, importedFileName);
    if (definitionText) {
      console.log(`---- ${importedFilePath} ----`);
      console.log(definitionText);
      console.log('---- End ----');
    }
  }
}

main();
