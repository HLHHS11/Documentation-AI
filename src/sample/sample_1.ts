import ts from 'typescript';
import * as fs from 'fs';
import * as path from 'path';

const options: ts.CompilerOptions = {
  target: ts.ScriptTarget.ESNext,
  module: ts.ModuleKind.CommonJS,
};

function parseSourceFile(filePath: string): ts.SourceFile {
  const code = fs.readFileSync(filePath, 'utf-8');
  return ts.createSourceFile(filePath, code, ts.ScriptTarget.ESNext, true);
}

function getImports(sourceFile: ts.SourceFile, resolver: ts.ModuleResolutionCache ): string[] {
  const imports: string[] = [];
  ts.forEachChild(sourceFile, (node) => {
    if (ts.isImportDeclaration(node)) {
      // const importText = node.getText(sourceFile);
      const moduleSpecifier = node.moduleSpecifier as ts.StringLiteral;
      const host = ts.createCompilerHost(options);
      // const resolvedModule = ts.resolveModuleName(moduleSpecifier.text, sourceFile.fileName, options, resolver);
      const resolvedModule = ts.resolveModuleName(moduleSpecifier.text, sourceFile.fileName, options, host, resolver);
      if (resolvedModule && resolvedModule.resolvedModule) {
        const importPath = resolvedModule.resolvedModule.resolvedFileName;
        imports.push(importPath);
      }
      // const importText = node.moduleSpecifier.getText(sourceFile);
      // imports.push(importText);
    }
  });
  return imports;
}

function getSourceCodeOfImportedFiles(mainFilePath: string, importPaths: string[]): Record<string, string> {
  const sourceCodes: Record<string, string> = {};

  importPaths.forEach((importPath) => {
    const resolvedPath = path.resolve(path.dirname(mainFilePath), importPath.replace(/['"]/g, ''));
    const sourceFile = parseSourceFile(resolvedPath);
    const sourceCode = sourceFile.getFullText();
    sourceCodes[resolvedPath] = sourceCode;
  });

  return sourceCodes;
}

function main() {
  const mainFilePath = '/home/yama/Documents/Programming/job-hunting/23インターン/chatwork/coding-test_20230726_1880984735695298560/src/app.ts';
  const mainSourceFile = parseSourceFile(mainFilePath);
  const resolver = ts.createModuleResolutionCache(path.dirname(mainFilePath), (x) => x)
  const imports = getImports(mainSourceFile, resolver);

  const sourceCodesOfImportedFiles = getSourceCodeOfImportedFiles(mainFilePath, imports);

  // インポートされているファイルのテキストを表示
  for (const [importedFilePath, sourceCode] of Object.entries(sourceCodesOfImportedFiles)) {
    console.log(`---- ${importedFilePath} ----`);
    console.log(sourceCode);
    console.log('---- End ----');
  }
}

main();
