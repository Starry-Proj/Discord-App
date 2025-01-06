import discord as Discord;

from discord.ui       import Button, View;
from discord.ext      import commands as Commands;  
from discord.ext      import commands as Commands;
from assets.functions import *;                     # Load our Functions
from assets.constants import *;                     # Load our Constant Variables

"""

    This file handles ALL free-to-use commands, here's a list:

    - buy - Returns the channel to purchase Starry Premium, along with an ad embed

    --

    Written: 1/5/2025

"""

class Premium(Commands.Cog):
    def __init__(self, App) -> None:
        self.App = App

    # Commands

    # -- Buy Command -- #

    @Commands.cooldown(1, 5, Commands.BucketType.user)
    @Commands.hybrid_command(name="buy",
                             description="Link the channel to purchase Starry premium")
    
    async def Buy(self, CTX: Commands.Context):
        """
        
            In short, this command will just be an advertisement lol,

            .. just hope the user actually buys Starry Premium!
        
        """

        Description: str = OpenFile("premium.md", "r")

        Embed: Discord.Embed = Discord.Embed(title="Starry Premium",
                                             description=Description,
                                             color=Discord.Color.green())
        
        NewViewer: View = View()

        ViewGithub: Button = Button(label="View Webpage", style=Discord.ButtonStyle.link, url="https://starry.luau.tech/")

        ButtonList: list = [ViewGithub]

        for Item in ButtonList:
            NewViewer.add_item(Item)

        await CTX.reply(embed=Embed, view=NewViewer, ephemeral=True)


# -- Setup the Cog -- #

async def setup(App) -> None:
    await App.add_cog(Premium(App))
