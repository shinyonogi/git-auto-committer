# GitHub Auto Contributer 🌱

楽〜にGitHub Contributionカレンダーの草を生やしまくりましょう！自動でテキトーなコミットメッセージを生成し、GitHubにプッシュします。

## 原理：
1. **main.py**を実行すると、**randomAddresses** フォルダに新しいファイルが作成されます
2. オプション：(OpenAI APIを使用して、適当にメッセージをGPTから取得します)
3. 自動生成されたメッセージ、またはデフォルトメッセージをファイルに書き込みます
4. オプション：(生成されたメッセージをLine BotやTelegram Botを介して通知します)
5. **git add, git commit, git push** を順次実行します

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
- `logging`

### 環境変数の設定 (オプション)

1. ルートディレクトリに **.env** ファイルを作成します。
2. .env 内で以下の環境変数を設定します：    　　
- **USE_OPENAI**: true or false (OpenAIのAPIを利用するか)
- **USE_LINE**: true or false (LINE Messaing APIを利用するか)
- **USE_TELEGRAM**: true or false (Telegram Messaing APIを利用するか)

- **OPENAI_API_KEY**: OpenAIのAPIキー (公式ホームページで取得)
- **TELEGRAM_BOT_TOKEN**: TelegramのBotトークン (BotFatherで取得)　　
- **TELEGRAM_CHAT_ID**: あなたのTelegram Chat ID (気合いで見つけます)
- **LINE_CHANNEL_ACCESS_TOKEN**: Line Developersから取得
- **LINE_USER_ID**: あなたのLineユーザーID (頑張って見つけます)

### Commit Message 自動生成

コミットメッセージはGPT-3.5-Turboを使用して自動生成することができます。メッセージの内容や詳細は、`generate_messages.py`内でカスタマイズ可能です。

### TelegramとLineの使用
生成されたメッセージをボット経由で自分に送信することができます。これを有効にするには、関連する環境変数を設定してください。

## Version 1.0 (Updated: 15.09.23)

一度の実行で、5〜15回の自動Commit & Pushを行います。

## 更にOptional...

MacのAutomatorを利用して、プログラムを日常的に自動実行することもできます（ローカル設定が必要です）。

