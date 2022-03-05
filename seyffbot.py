import discord
import os
from dotenv import load_dotenv
from discord.ext import commands

# Token laden
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

#Bot-Settings
bot = discord.Bot()

@bot.event
async def on_ready():
    print(f"We have logged in as {bot.user}")

@bot.slash_command(guild_ids=[931187178980126780])
async def hello(ctx):
    await ctx.respond("Hello!")

bot.run("TOKEN")