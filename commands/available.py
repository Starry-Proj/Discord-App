import discord as Discord;
import os      as OS;

from discord.ext import commands as Commands;
from assets.functions import *;               # Load our Functions
from assets.constants import *;               # Load our Constant Variables

"""

    This file handles ALL free-to-use commands, here's a list:

    - script - Returns the current loadstring
    - invite - Returns the invite link for Starry's Discord server
    - ticket - Returns the channel to create a ticket, for users who can't find it

    --

    Written: 1/5/2025

"""

class Available(Commands.Cog):
    def __init__(self, App) -> None:
        self.App = App


    # Commands

    # ...


# -- Setup the Cog -- #

async def setup(App) -> None:
    await App.add_cog(Available(App))