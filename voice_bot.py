import discord
import os
from discord.ext import commands

# 動作確認用 
print("OK")

# インテントの設定（ボイス状態を検知するために必要）
intents = discord.Intents.default()
intents.voice_states = True
intents.members = True  # メンバー情報も取得できるように

# Botの起動設定（コマンド接頭辞は使用しない）
bot = commands.Bot(command_prefix="!", intents=intents)

# Botがオンラインになったときに表示
@bot.event
async def on_ready():
    print(f"Bot is ready. Logged in as {bot.user}")

# ボイスチャンネルの入室を検知
@bot.event
async def on_voice_state_update(member, before, after):
    if before.channel is None and after.channel is not None:
        # 入室したときの処理
        text_channel = discord.utils.get(member.guild.text_channels, name="bot通知")  # チャンネル名を指定
        if text_channel:
            await text_channel.send(f"@everyone {member.display_name} がボイスチャンネルに参加しました！")

# ここに自分の Bot トークンを貼り付けてください（"..."の部分）
TOKEN = os.getenv("DISCORD_TOKEN")
print("TOKEN:", TOKEN)  # ← デバッグ用。動作確認後は削除推奨。
client.run(TOKEN)
