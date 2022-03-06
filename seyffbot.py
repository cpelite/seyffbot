import nextcord
import os
from dotenv import load_dotenv
from nextcord.ext import commands

# Token laden
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

#intents festlegen
intents = nextcord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix='$', intents=intents)

#bot-version
@bot.command()
async def botinfo(ctx):
    embed=nextcord.Embed(title="Informationen über den Bot.")
    embed.add_field(name="Bot-Version", value="Beta 1 - Albert I.")
    embed.add_field(name="Verwendete Python-Version", value="3.10.2")
    embed.add_field(name="Entwickler", value="Ihr kennt den verrückten doch.")
    await ctx.send(embed=embed)

#falls command nicht existiert.
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        embed = nextcord.Embed(title="Sorry!")
        embed.add_field(name="Es tut mir leid..", value = "...aber dieser Befehl existiert noch nicht.")
        await ctx.send(embed=embed)

bot.run(TOKEN)