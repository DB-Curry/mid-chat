# Mid Chat

このボットは、ユーザーの入力に基づいてOpenAIのGPTモデルを使用し、Midjourneyのプロンプトを生成するDiscordボットです。
これを導入すれば、会話形式でpromptの修正ができます。

## セットアップ

1. このリポジトリをクローンしてください。

2. 必要な依存関係をインストールします：
   ```
   pip3 install -r requirements.txt
   ```

3. プロジェクトのルートディレクトリに `.env` ファイルを作成し、以下の内容を記入してください：
   ```
   DISCORD_TOKEN=あなたのDiscordボットトークン
   OPENAI_API_KEY=あなたのOpenAI APIキー
   ```
   `あなたのDiscordボットトークン` と `あなたのOpenAI APIキー` を実際のトークンとAPIキーに置き換えてください。

## ボットの実行

以下のコマンドでボットを実行します：
```
python3 main.py
```

## 使用方法

Discord Botを用意してください。

このあたりの記事を参考にDiscord Developer Portalで作ります。

- https://qiita.com/shown_it/items/6e7fb7777f45008e0496

スクリプトを実行し、ログイン状態にすることで、botの準備は完了です。

<br>

Discordチャンネルで用意したボットにメンションし、どのような絵を描きたいか話しかけてください。ボットはあなたの入力に基づいてMidjourneyプロンプトを生成します。

もしプロンプトを調整したければ、同じようにメンションで修正依頼できます。

会話を保存しているので最新5メッセージは覚えています。

## 使用例
<br>
botにメンションすると、プロンプトが送られてくるので、それをmidjournyで生成する。
<br>
<br>

![スクリーンショット 2024-08-10 145718](https://github.com/user-attachments/assets/b5ea4abf-c129-433c-bd24-c2848c50e500)

<br>
<br>
修正したいときは、変更内容をbotに伝えると改良されたプロンプトが送られてくる。
<br>
<br>

![スクリーンショット 2024-08-10 145812](https://github.com/user-attachments/assets/837a33ff-3d04-481a-b4ee-c01f3deda560)

### 「月の爆撃機」
![low_res_image](https://github.com/user-attachments/assets/15bf9ad1-2501-49fe-bdb3-3daa4bd51f44)


### 「この爆撃機は流線型のフォルムをしています」
![low_res_image_2](https://github.com/user-attachments/assets/9de35b4e-820e-44b1-b0b1-f315722d4ce1)


## ライセンス

このプロジェクトはオープンソースで、誰でも自由に使用、修正、配布することができます。帰属表示は必要ありません。
