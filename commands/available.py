import discord as Discord;

from discord.ui       import Button, View;
from discord.ext      import commands as Commands;
from assets.functions import *;                     # Load our Functions
from assets.constants import *;                     # Load our Constant Variables

"""

    This file handles ALL free-to-use commands, here's a list:

    - script - Returns the current loadstring
    - invite - Returns the invite link for Starry's Discord server
    - help   - Returns an embed that lets you scroll through every command
    - games  - Returns every support game for Starry

    --

    Written: 1/5/2025 - 1/10/2025

"""

# -- Classes -- #

class Available(Commands.Cog):
    def __init__(self, App) -> None:
        self.App = App

    # Commands

    # -- Invite Command -- #

    @Commands.cooldown(1, 5, Commands.BucketType.user)
    @Commands.hybrid_command(name       ="invite",
                             description="Generate a permanent invite to the server")
    
    async def Invite(self, CTX: Commands.Context) -> None:
        Embed: Discord.Embed = Discord.Embed(title="Server Invite",
                              description=f"{CustomEmojis["Check"]}{Whitespace} Here's your permanent invite to Starry")
        
        Settings: dict = {
            "reason": "Starry Invite",
            "age" : 0,
            "uses" : 0,
            "temp" : False,
            "unique": False
        }

        Channel: Discord.TextChannel = CTX.channel
        Invite: Discord.Invite = Channel.create_invite(reason=Settings["reason"], max_age=Settings["age"], max_uses=Settings["uses"], temporary=Settings["temp"], unique=Settings["unique"])

        Converted: str = str(await Invite)

        def CleanseInvite(Code: str) -> str:
            assert isinstance(Code, str), "Code should be of type \"str\""

            return str.replace(Code, "https://", "")

        Cleansed: str = CleanseInvite(Converted)

        Embed.add_field(name="", value=f"**{Cleansed}**")

        await CTX.reply(embed=Embed)


    # -- Games Command -- #

    @Commands.cooldown(1, 5, Commands.BucketType.user)
    @Commands.hybrid_command(name       = "games",
                             description="All of the supported games for Starry")
    
    async def Games(self, CTX: Commands.Context) -> None:
        Description: str = OpenFile("games.md", "r")

        Embed = Discord.Embed(title="Starry's Supported Games",
                              description=Description,
                              color=Discord.Color.blurple())
        
        NewViewer: View = View()
        
        RawScript: Button = Button(label="Get Script",  style=Discord.ButtonStyle.success)
        RawScript.callback = RawCallback

        await CTX.reply(embed=Embed, view=NewViewer, delete_after=30)


    # -- Script Command -- #

    @Commands.cooldown(1, 5, Commands.BucketType.user)
    @Commands.hybrid_command(name       ="script",
                             description="Returns Starry's latest & updated script")
    
    async def Script(self, CTX: Commands.Context) -> None:
        Embed: Discord.Embed = Discord.Embed(title="Script",
                              description="For mobile users, press the **\"Raw\"** button and copy the message sent",
                              color=Discord.Color.blurple())
        
        NewViewer: View = View()
        
        RawScript: Button = Button(label="Raw Script",  style=Discord.ButtonStyle.success)
        RawScript.callback = RawCallback

        ViewGithub: Button = Button(label="View Github", style=Discord.ButtonStyle.link, url="https://github.com/Starry-Proj")

        ButtonList: list = [RawScript, ViewGithub]

        for Item in ButtonList:
            NewViewer.add_item(Item)

        Embed.add_field(name ="", value=f"> ```lua{Newline}> {GetScript()}{Newline}> ```")

        await CTX.reply(embed=Embed, view=NewViewer, delete_after=30)


# -- Assign Button Callbacks -- #

async def RawCallback(Interaction: Discord.Interaction) -> None:
    return await Interaction.response.send_message(GetScript(), ephemeral=True)


# -- Setup the Cog -- #

async def setup(App) -> None:
    await App.add_cog(Available(App))
