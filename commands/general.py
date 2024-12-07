import discord as Discord
import os as OS

from modules.functions import *
from constants import *
from discord.ext import commands as Commands

class General(Commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @Commands.cooldown(1, 10, Commands.BucketType.user)
    @Commands.hybrid_command(name="buy",
                             description="Sets everything up for you to buy Starry")
    async def buy(self, CTX: Commands.Context):
        guilds = OS.getenv("WHITELISTED", "").split(",")
        
        for id in guilds:
            try:
                if CTX.guild.id != int(id.strip()):
                    return await CTX.reply(embed=errorEmbed(Discord.Color.red(),
                                           "Message Purge ‎ <a:bonk:1289335115045928981>",
                                           "You are not allowed to use this command in this server.\n- To use this app, join the Starry server!\n\nInvite: [disсord.gg/zyXZSn97hN](https://discord.gg/zyXZSn97hN)"))
            
            except ValueError:
                continue

    @Commands.cooldown(1, 5, Commands.BucketType.user)
    @Commands.hybrid_command(name="script",
                             description="Get the latest script for Starry")
    async def script(self, CTX: Commands.Context):
        guilds = OS.getenv("WHITELISTED", "").split(",")
        
        for id in guilds:
            try:
                if CTX.guild.id != int(id.strip()):
                    return await CTX.reply(embed=errorEmbed(Discord.Color.red(),
                                           "Message Purge ‎ <a:bonk:1289335115045928981>",
                                           "You are not allowed to use this command in this server.\n- To use this app, join the Starry server!\n\nInvite: [disсord.gg/zyXZSn97hN](https://discord.gg/zyXZSn97hN)"))
            
            except ValueError:
                continue

        await CTX.defer()
        class ScriptView(Discord.ui.View):
            @Discord.ui.button(label="Give Raw Script", style=Discord.ButtonStyle.primary)
            async def giveRaw(self, interaction: Discord.Interaction, button: Discord.ui.Button):
                await interaction.response.send_message(content=script, ephemeral=True)

        await CTX.reply(embed=successEmbed(None,
                                           "Script",
                                           "[Press me](https://discord.com/channels/1258712305332523028/1314128299537993778) to see if your executor is supported\n- n' [view here](https://discord.com/channels/1258712305332523028/1314622738706595881) to see the supported games",
                                           "This command is available to all users.",
                                           fields=[
                                               ["Script", f"{backticks}lua\n{script}\n{backticks}", False]
                                           ]),
                                           view=ScriptView())

async def setup(bot):
    await bot.add_cog(General(bot))
