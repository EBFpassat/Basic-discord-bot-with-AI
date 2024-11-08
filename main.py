import discord
from discord.ext import commands
from model import predict
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)
@bot.command()
async def kontrol(ctx):
    if ctx.message.attachments:
        for fotograf in ctx.message.attachments:
            file_name = fotograf.filename
            file_url = fotograf.url
            await fotograf.save(f'./images/{file_name}')
            await ctx.send(predict(imagePath= f"./images/{file_name}"))
    else:
        await ctx.send('Fotoğraf Göndermeyi Unuttunuz!')

bot.run("YOUR TOKEN HERE")