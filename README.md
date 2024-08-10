# Discord Bot with OpenAI Integration

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
python3 bot.py
```

## 使用方法

Discordチャンネルでボットにメンションし、プロンプトを提供してください。ボットはあなたの入力に基づいてMidjourneyプロンプトを生成します。

## ライセンス

このプロジェクトはオープンソースで、誰でも自由に使用、修正、配布することができます。帰属表示は必要ありません。