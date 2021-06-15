# import discord                      # discord.py
from discord.ext import commands    # commands framework
import config                       # config_file
import os, datetime                 # 標準モジュール
import scrape                       # スクレイピングファイル

# 環境変数からtokenを取得
token = os.environ["DISCORD_SELF_MADE_BOT_TOKEN"]

# 蔵のインスタンスを作成
bot = commands.Bot(command_prefix = config.prefix)

# 起動時のイベント
@bot.event
async def on_ready():
    print("Botを起動しました")

# 教員の情報をスクレイピングから取り出すコマンド
@bot.command()
async def teacher(ctx, teacher_name, find_info):
    await ctx.channel.send(scrape.getInfo(teacher_name, find_info))

# helloコマンド
@bot.command()
async def hello(ctx):
    await ctx.channel.send("こんにちは")
    return

# 現在時刻コマンド
@bot.command()
async def time(ctx):
    await ctx.channel.send(f"現在は {datetime.datetime.now()} です")
    return

# メッセージを送ったときの反応
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    
    await bot.process_commands(message)

bot.run(token)
