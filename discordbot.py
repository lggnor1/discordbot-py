import discord
from discord.ext import commands
import asyncio

# 인텐트 설정
intents = discord.Intents.default()
intents.messages = True
intents.guilds = True
intents.message_content = True

# 봇 설정
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():  # 봇이 실행되면 한 번 실행됨
    print("이 문장은 Python의 내장 함수를 출력하는 터미널에서 실행됩니다\n지금 보이는 것 처럼 말이죠")
    await bot.change_presence(status=discord.Status.online, activity=discord.Game("청소"))

@bot.command()
@commands.has_permissions(administrator=True)
async def 청소(ctx, amount: int):
    await ctx.message.delete()
    await ctx.channel.purge(limit=amount)

    embed = discord.Embed(
        title="메시지 삭제 알림",
        description=f"채팅 {amount}개가 삭제 되었습니다",
        color=0x000000
    )
    message = await ctx.send(embed=embed)
    await asyncio.sleep(3)
    await message.delete()

@청소.error
async def 청소_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.message.delete()
        message = await ctx.send(f"{ctx.author.mention}, 당신은 명령어를 사용할 수 있는 권한이 없습니다")
        await asyncio.sleep(3)
        await message.delete()

# 봇을 실행시키기 위한 토큰을 작성해주는 곳
bot.run('MTIxNjMxNTUwNjI2NTY5MDExNQ.GJNLkU.0sLW7dZ7iuBLNBtKwLsPZjmWmXFIPD0cI1ZHpQ')
