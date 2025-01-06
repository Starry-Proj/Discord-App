import dotenv  as ENV;
import discord as Discord;
import os      as OS;
import asyncio as Async;

from dotenv           import load_dotenv;   # Load our Environment Variables
from assets.functions import *;             # Load our Functions
from assets.events    import *;             # Load our Bot Events
from assets.errors    import *;             # Load our Error Handling Data

load_dotenv()

"""

    This is our main file, which brings everything together.

    This file will **never** have to be updated, unless you want to add more features.

    --

    Written: 1/4/2025

"""


# Variables

TOKEN = OS.getenv("TOKEN")

Client = GetClient()


# -- Setup Syncing -- #

@Client.command(name="sync")
async def Sync(CTX: Commands.Context) -> None:
    await Client.tree.sync()

    for Name in OS.listdir("./commands"):
        if Name.endswith(".py"):
            try:
                await Client.reload_extension(f"commands.{Name[:-3]}")

                print(f"{Emojis["Gear"]} Reloaded {Name[:-3]} Cog")

            except Exception as Error:
                print(f"{Emojis["X"]} Error reloading {Name[:-3]} Cog: {Error}")

    Message = f"Everything was synced to the command tree! {Newline}{Newline} 1. Reload Discord using **CTRL + R** or **CMD + R** on macOS {Newline} 2. On Mobile, simply close & re-open Discord. {Newline}{Newline}-# **NOTE**: Still having issues? Contact [@Suno](<https://discord.com/users/1002377371892072498>)"

    Embed = Discord.Embed(title="Synced Commands",
                          description=Message,
                          color=Discord.Color.green())

    print(f"{Newline}{Emojis["Rocket"]} Synced all Cogs{Newline}")

    RemoveCache()
    
    await CTX.reply(embed=Embed, delete_after=5)


# -- Setup the Cogs -- #

for Name in OS.listdir("./commands"):
    if Name.endswith(".py"):
        Async.run(Client.load_extension(f"commands.{Name[:-3]}"))

        print(f"{Emojis["Gear"]}{Whitespace} Loaded {Name[:-3]} Cog")


# -- Event Handling -- #

print()

SetupEvents(); ErrorHandling()


# -- Run the Bot -- #

Client.run(TOKEN)

print(f"{Newline}{Emojis["X"]} Starry closed & App is offline {Newline}") # This exclusively runs after the process is killed
