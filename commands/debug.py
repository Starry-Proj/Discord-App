import discord as Discord
import os as OS

from modules.functions import *
from discord.ext import commands as Commands

class Debug(Commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @Commands.cooldown(1, 5, Commands.BucketType.user)    
    @Commands.hybrid_command(name="ping",
                             description="Returns the speed of the Starry bot")
    async def ping(self, CTX: Commands.Context):
        guilds = [1258712305332523028, 1313705848404574309]
        
        for id in guilds:
            try:
                if CTX.guild.id != int(id.strip()):
                    return await CTX.reply(embed=errorEmbed(Discord.Color.red(),
                                           "Starry Police ‎ <a:bonk:1289335115045928981>",
                                           "You are not allowed to use this command in this server.\n- To use this app, join the Starry server!\n\nInvite: [disсord.gg/zyXZSn97hN](https://discord.gg/zyXZSn97hN)"))
            
            except ValueError:
                continue
        
        ping = round(self.bot.latency * 1000)
        isGood = ping < 100
        ifIsGood = "good" if isGood else "bad"

        await CTX.reply(embed=successEmbed(None,
                                          "Pong! ‎ <a:hellokittyjump:1259226726639206415>",
                                          f"Starry's latency is {ping}ms, this is considered a {ifIsGood} connection speed.",
                                          None), delete_after=3)

async def setup(bot):
    await bot.add_cog(Debug(bot))