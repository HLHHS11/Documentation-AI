# Documentation-AI
技育展2023近畿ブロック予選の登壇作品`TypeScriptの開発補助AIエージェント`改め，`Pythonドキュメンテーション生成AI`のリポジトリです。  
当日の時間ギリギリまで制作してなんとか完成させたもので，まだまともに`README.md`が書けていません…。  
**もしこのリポジトリをご覧になってくださった方で「早速使ってみたい！」という方がいらっしゃれば，個別に説明いたしますので[Twitter](https://twitter.com/YAMAnoKUCHI_)で一声おかけください！待ってます！！**  
- [**登壇資料**](https://onedrive.live.com/edit.aspx?resid=27A40157802CF400!238738&ithint=file%2cpptx&ct=1691746036945&wdOrigin=OFFICECOM-WEB.MAIN.MRU)
## 環境構築
``` sh
# リポジトリのクローン
git clone https://github.com/HLHHS11/Documentation-AI.git
# Python仮想環境の構築
python3 -m venv venv
# 仮想環境をアクティベート
source venv/bin/activate # Windowsの場合venv\Scripts\activate
pip install -r requirements.txt
```
## 使い方
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
