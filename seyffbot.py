import discord
import os
from dotenv import load_dotenv
from discord.ext import commands

# Token laden
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

#intents festlegen
intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix='$', intents=intents)

#load extensions
bot.load_extension("commands")
bot.load_extension("gifs")

#bot-version
@bot.command()
async def botinfo(ctx):
    embed=discord.Embed(title="Informationen über den Bot.")
    embed.add_field(name="Bot-Version", value="Beta 1 - Albert I.")
    embed.add_field(name="Entwickler", value="Ihr kennt den verrückten doch.")
    await ctx.send(embed=embed)

#falls command nicht existiert.
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        embed = discord.Embed(title="Sorry!")
        embed.add_field(name="Es tut mir leid..", value = "...aber dieser Befehl existiert noch nicht.")
        await ctx.send(embed=embed)

bot.run(TOKEN)