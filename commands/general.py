import discord as Discord

from discord.ext import commands as Commands

class General(Commands.Cog):
    def __init__(self, bot):
        self.bot = bot

async def setup(bot):
    await bot.add_cog(General(bot))