# 導入Discord.py
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.typing = False
intents.presences = False

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
#當機器人完成啟動時
async def on_ready():
    print('目前登入身份：', bot.user)

@bot.event
async def on_member_join(member):
    print(f'{member} join!')


@bot.command(pass_context=True)
@bot.event
async def on_member_join(ctx, member):
    print(f'{member} has joined a server.')
    await ctx.send(f"Hello {member}!")
    await ctx.member.send(f"Welcome to the server!")

# Token
token = ("MTA0ODQzMjYzNjQwNzg0MDc3OA.GGtCSs.JpWB5su08_cLP90s-BwAvSlTZFb2D3PZ5TMuSU")
bot.run(token)