import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

client = OpenAI(
  api_key=OPENAI_API_KEY,
)

# インテントの設定
intents = discord.Intents.default()
intents.message_content = True

# ボットの初期化
bot = commands.Bot(command_prefix='!', intents=intents)

chat_history = []
MAX_HISTORY = 6  # 各ユーザーの最大履歴保存数

init_message = [{"role": "system", "content": "You are a helpful assistant that generates Midjourney prompts based on user input. Create detailed and creative prompts that will result in interesting images.Prompts should be output in English.Please do not add parameters as much as possible."}]

# init_messageを会話履歴に追加
chat_history.extend(init_message)

@bot.event
async def on_ready():
    print(f'{bot.user} としてログインしました。')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    
    #botへのメンションがない場合、処理を終了
    if f'<@{bot.user.id}>' not in message.content:
        return 

    # メンションを除去してユーザー入力を取得
    user_input = message.content.replace(f'<@{bot.user.id}>', '').strip()
    
    # ユーザーの入力が空でない場合、会話履歴に追加
    if user_input:
        chat_history.append({"role": "user", "content": user_input})
        # 会話履歴が最大数を超えた場合、最も古いメッセージを削除する。ただし、init_messageは削除しない
        if len(chat_history) > MAX_HISTORY:
            chat_history.pop(1)
    else:
        return
    
    try:
        # GPTを使用してプロンプトを生成
        completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=chat_history
        )
        
        generated_prompt = completion.choices[0].message.content

        # 生成されたプロンプトをDiscordに送信
        await message.channel.send(f"```\n{generated_prompt}\n```")
        
        # 生成されたプロンプトを会話履歴に追加
        chat_history.append({"role": "system", "content": generated_prompt})
        
    except Exception as e:
        await message.channel.send(f"An error occurred: {str(e)}")

# ボットを実行
if __name__ == "__main__":
    bot.run(TOKEN)
