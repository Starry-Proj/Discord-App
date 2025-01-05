import discord as Discord;
import os      as OS;

from discord.ext import commands as Commands;
from assets.functions import *;               # Load our Functions
from assets.constants import *;               # Load our Constant Variables

"""

    This file handles ALL free-to-use commands, here's a list:

    - ban <member> <reason>     - Bans a member from the server
    - kick <member> <reason>    - Kicks a member from the server
    - mute <member> <reason>    - Mutes a member in the server
    - unmute <member>           - Unmutes a member in the server
    - warn <member> <reason>    - Warns a member in the server
    - unwarn <member>           - Unwarns a member in the server
    - clear <amount>            - Clears a certain amount of messages in the channel
    - lock                      - Locks the channel
    - unlock                    - Unlocks the channel

    --

    Written: 1/5/2025

"""

class Admin(Commands.Cog):
    def __init__(self, App) -> None:
        self.App = App


    # Commands

    # ...


# -- Setup the Cog -- #

async def setup(App) -> None:
    await App.add_cog(Admin(App))