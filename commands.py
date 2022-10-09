#Imports
import nextcord
from nextcord.ext import commands

class facts(commands.Cog):
    def __init__(self,seyffbot):
        self.bot = seyffbot

    @commands.command()
    async def factsheet(self, ctx):
        embed = nextcord.Embed(title="Fakten über das Vereinigte Nordhanarische Kaiserreich")
        embed.add_field(name="Residenzstadt", value="Syffia")
        embed.add_field(name="Regierungssitz", value="Frankenthal")
        embed.add_field(name="Staatsform", value="konstitutionell-parlamentarische Monarchie")
        embed.add_field(name="Nordhanarische Kaiser", value="Albert I.")
        embed.add_field(name="Nordhanarischer König", value="vakant")
        embed.add_field(name="Regierungschef", value="Staatskanzler Sebastian von Hammer")
        await ctx.send(embed=embed)
        return

    #setup
    def setup(bot):
        bot.add_cog(facts)