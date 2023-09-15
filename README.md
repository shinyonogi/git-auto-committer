# Git Auto Committer 🌱

楽〜にGitHub Contributionカレンダーの草を生やしまくりましょう！自動でテキトーなコミットメッセージを生成し、GitHubにプッシュします。

## 原理：
1. **main.py**を実行すると、**randomAddresses** フォルダに新しいファイルが作成されます。
2. OpenAI APIを使用して、適当にメッセージをGPTから取得します。
3. このメッセージをファイルに書き込みます。
(4. 生成されたメッセージをLine BotやTelegram Botを介して通知します。)
5. **git add, git commit, git push** を順次実行します。

## 使い方:

### モジュール

Pythonのライブラリ/モジュールがいくつか必要です。必要であれば、`pip install`を使ってインストールして下さい。

※現時点で必要なもの達です。

- `os`
- `random`
- `requests`
- `openai`
- `linebot`
- `from pathlib Path`

### 環境変数の設定

1. ルートディレクトリに **.env** ファイルを作成します。
2. .env 内で以下の環境変数を設定します：  　　
- **OPENAI_API_KEY**: OpenAIのAPIキー (公式ホームページで取得)

オプション：
- **TELEGRAM_BOT_TOKEN**: TelegramのBotトークン (BotFatherで取得)　　
- **TELEGRAM_CHAT_ID**: あなたのTelegram Chat ID (気合いで見つけます)
- **LINE_CHANNEL_ACCESS_TOKEN**: Line Developersから取得
- **LINE_USER_ID**: あなたのLineユーザーID (頑張って見つけます)

### Commit Message 自動生成

メッセージはGPT-3.5-Turboを使用して生成されますが、`generate_messages.py`内でカスタマイズ可能です。

### TelegramとLineの使用
生成されたメッセージをボット経由で自分に送信することができます。これを有効にするには、関連する環境変数を設定し、`main.py`のコメントアウト部分を解除してください。

## Version 1.0 (Updated)

一度の実行で、5〜15回の自動Commit & Pushを行います。

## 更にOptional...

MacのAutomatorを利用して、プログラムを日常的に自動実行することもできます（ローカル設定が必要です）。

