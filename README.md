# cdle_youth_handson_app_1

## 使い方

### Git
```
# ターミナル上
# git上のファイルを取得
git clone [URL]
# ブランチを作成して切り替える
git checkout -b [ブランチ名]
# 作成・変更した全ファイルをadd
git add .
# addしたファイルをcommit(コメント付き)
git commit -m "コメント"
# ブランチを確認(次の操作でpushするブランチを確認しておく)
git branch -a
# commitしたファイルをgitにpush
git push origin [ブランチ名]
```

### Docker
GitでcloneしてきたファイルからDockerを立ち上げる

```
# docker-compose.ymlというファイルが置いてある場所で以下を実行
# imageを作成して、コンテナを立ち上げるコマンド
# 初回とdocker-compose.yml, Dockerfile, requirements.txtを変更した際に--buildをつける
docker-compose up -d --build
# 2回目以降に、上記のファイルに変更がない場合は以下を実行すればコンテナが起動する
docker-compose up -d
# 起動したコンテナに入る
docker exec -it django_cdle_app bash
```

### Python
Python(Django)のコマンド  
基本的に、pythonのコマンドはコンテナに入ることで使うことができる  
プロジェクトやアプリケーションは作成済みなので実行の必要はない

```
# DBのマイグレーション(多分初回の実行はしなくても大丈夫だと思いますが一応実行してください)
python manage.py migrate
# サーバーの起動
python manage.py runserver 0:8000
```

### ファイル構成
source/ChatBotAppの直下に編集するファイルがある（※ChatBotAppフォルダは上位下位で2つあるが、以降で出てくるものは下位の層にあるものを指す）  

#### ChatBotProject
- settings.py
  - pathなどの設定を書くファイル
- urls.py
  - 後で出てくるurls.pyで設定されたurlのベースのurlを設定するファイル

#### ChatBotApp
- views.py
  - viewを定義するファイル
- models.py
  - model(DBの設計)を定義するファイル
- forms.py
  - form（データの送信など）を定義するファイル
- urls.py
  - それぞれのページのurlを定義するファイル

#### templates
htmlファイルを管理するためのフォルダ  
htmlファイルは自動的にtemplatesから読み込まれるように設定してある
- login
  - base.html: 全体の共通部分を書くためのファイル
  - login.html: ログイン画面
  - register.html: ユーザー作成画面
- rooms
  - base.html
  - my_page.html: マイページ
  - room_〜.html: 各チャットボットのルーム

#### static
静的ファイルを管理するためのフォルダ  
img、css、jsのフォルダを作成済み　　

#### media  
ユーザーから送信されたファイル（画像など）を管理するフォルダ  
アイコンを管理するためのuser_iconsというフォルダを作成済み

### ライブラリを追加したい時
requirements.txtにいれて、再ビルドすることでライブラリをコンテナに入れることができる  
(作業が進むにつれてbuildが大変になるので、buildせずに更新できるようにできたらいいかもしれない)  
参考：[dockerのpythonコンテナをビルドしなおさずpip installでライブラリを更新できるようにする方法 ](https://asukiaaa.blogspot.com/2020/07/docker-python-pip-install-without-rebuilding.html)