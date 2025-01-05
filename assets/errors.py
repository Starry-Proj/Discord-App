import dotenv  as ENV;
import discord as Discord;
import os      as OS;
import asyncio as Async;

from dotenv           import load_dotenv;   # Load our Environment Variables
from assets.functions import *;             # Load our Functions
from assets.events    import *;             # Load our Bot Events

"""

    This file is designed to be our main error handler,

    & basically, in short when a command errors, we'll handle it here...

    & make it so it doesn't return a traceback (or in the user's case, an Infinite Yield Error)

    --

    Written: 1/5/2025

"""

# Variables

Client = GetClient()


# -- Error Handling -- #

def ErrorHandling():
    """
    
        This is the ONLY event outside of `./events.py`,
        
        everything else is in that file.
    
    """
    
    @Client.event
    async def on_command_error(CTX: Commands.Context, Error: str) -> None:
        print(f"{Newline}{Emojis["X"]} Something Came Up: {Error}")

        Embed = Discord.Embed(title="Uh Oh..",
                            description=f"Something came up when processing your command, {Newline}- if it's anything about a cooldown, **disregard this message**",
                            color=Discord.Color.yellow())
        
        Embed.add_field(name="Error Message", value=f"```{Newline}{Error}{Newline}```")

        await CTX.reply(embed=Embed, delete_after=15)