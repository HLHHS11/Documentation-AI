# Documentation-AI
技育展2023近畿ブロック予選の登壇作品`TypeScriptの開発補助AIエージェント`改め，`Pythonドキュメンテーション生成AI`のリポジトリです。技育展決勝大会での発表に向けて，さらなる開発に取り組んでいます！  
当日の時間ギリギリまで制作してなんとか完成させたもので，まだまともに`README.md`が書けていません…。  
**もしこのリポジトリをご覧になってくださった方で「早速使ってみたい！」という方がいらっしゃれば，個別に説明いたしますので[Twitter](https://twitter.com/YAMAnoKUCHI_)で一声おかけください！待ってます！！**  
- [**登壇資料**](https://onedrive.live.com/edit.aspx?resid=27A40157802CF400!238738&ithint=file%2cpptx&ct=1691746036945&wdOrigin=OFFICECOM-WEB.MAIN.MRU)

## なにができる！？
このプログラムにソースコードを読み込ませると，うまく情報を整理してLLMに渡すことで，自動でドキュメントを生成してくれます！現在の対応言語はPythonです。  
具体的な仕組みは以下の通りです。
1. 解析対象のソースコードを"抽象構文木（AST）"ライブラリで読み込んで，シンボル（関数・クラス・変数など）間の依存関係を抽出する。  
   こうして"有向非巡回グラフ（DAG）"が得られることが期待され，それをトポロジカルソートすることで依存関係を解決する。
1. これを用いて依存関係のないシンボルから順次ドキュメント生成を行う。  
   依存関係をもつシンボルについても，そのソースコードを依存先シンボルのドキュメント（**※すでに生成済み！**）と一緒にLLM渡すことで，正しいコンテキスト理解のもとでドキュメント生成を行うことができる。


## 使い方
### セットアップ
``` sh
# リポジトリのクローン
git clone https://github.com/HLHHS11/Documentation-AI.git
# Python仮想環境の構築
python3 -m venv venv
# 仮想環境をアクティベート
source venv/bin/activate # Windowsの場合venv\Scripts\activate
pip install -r requirements.txt
# SQLiteのインストール
sudo apt-get install sqlite3
```
また，`.env`ファイルにより`OPENAI_API_KEY`を指定してください。（参考: [.env.sample](./.env.sample)）
### プログラムの開始
``` sh
# 仮想環境をアクティベート
source venv/bin/activate
# プログラムの開始
python -m documentationAI
```
以上のコマンド入力を行うと，コマンド入力画面が出てきますので，`documentation`と入力してください。  
```
Welcome to Documentation-AI!
Type 'help' for available commands or 'exit' to quit.
>>
```
続いて，解析を行いたいPythonプロジェクトのルートディレクトリの絶対パスとパッケージ名を入力してください。  
たとえば当プロジェクトを解析する場合，それぞれルートディレクトリ: [`.`](.)を表す絶対パス，パッケージ名: `documentationAI`を入力してください。
```
Welcome to Documentation-AI!
Type 'help' for available commands or 'exit' to quit.
>> documentation
Starting documentation generator...
Enter the absolute dilectory path to generate documentation for:
    <PROJECT_ROOT_ABS_PATH>
Enter the python package name:
    <PACKAGE_NAME>
```
これらの操作を行うと，[`./generated_documentation`](./generated_documentation)内の該当ディレクトリ内に，順次ドキュメントが生成・格納されていきます。

## 今後の展望
- 他言語対応したい！  
  抽象クラスを用いて処理の枠組みを抽象化することで，将来的な多言語対応にそなえています。
- 自動ドキュメント生成機能の柔軟性UP  
  現状，ドキュメント生成は最初から最後まで一気に行っています。すなわち，ソースコードの追加・修正に全く対応できていません。データの保存形式の工夫や，IDEとの連携などにより，変更を検知した部分のみドキュメント更新を行う仕組みが必要です。
- 自動ドキュメント生成機能以外の機能追加  
  自動ドキュメント生成機能だけがこのプログラムの強みではありません。これをうまく利用して，様々な機能を実現したいと考えています！
  - 対話インターフェース（AIと開発に関する悩み事を相談）
  - コード自動生成（対話の結果としてソースコード生成）
  - テスト自動生成
  - コード最適化の提案
  - GUIの提供
