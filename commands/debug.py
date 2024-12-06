import discord as Discord

from modules.functions import *
from discord.ext import commands as Commands

class Debug(Commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @Commands.cooldown(1, 5, Commands.BucketType.user)    
    @Commands.hybrid_command(name="ping",
                             description="Returns the speed of the Starry bot")
    async def ping(self, CTX: Commands.Context):
        ping = round(self.bot.latency * 1000)
        isGood = ping < 100
        ifIsGood = "good" if isGood else "bad"

        await CTX.reply(embed=successEmbed(None,
                                          "Pong! ‎ <a:hellokittyjump:1259226726639206415>",
                                          f"Starry's latency is {ping}ms, this is considered a {ifIsGood} connection speed.",
                                          None), delete_after=3)

async def setup(bot):
    await bot.add_cog(Debug(bot))