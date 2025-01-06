import discord as Discord;
import os      as OS;

from discord.ext import commands as Commands;
from .constants  import *;                       # Load our Constant Variables

"""

    This script is aimed towards GETTER and possible SETTER functions.

    Mainly to just get information though.

    --

    Written: 1/4/2025

"""

# Variables

Client = Commands.Bot(command_prefix="$",
                      intents=Discord.Intents.all())

Script = f"loadstring(game:HttpGet(\"https://luau.tech/build\"))()"


# -- GENERAL FUNCTIONS -- #

def FormatNumber(number: int) -> str:
    """
    
        This function will turn something like 1000 into 1,000.
    
    """

    Formatted = "{:,}".format(number)

    print(f"{Newline}{Emojis["Book"]} Formatted number: {Formatted}{Newline}")

    return Formatted

def RemoveCache():
    for Root, _, Files in OS.walk("."):
        if "__pycache__" in Root:
            for File in Files:
                OS.remove(f"{Root}/{File}")

            OS.rmdir(Root)


# -- GETTERS -- #

def GetClient() -> None:
    return Client

def GetScript() -> None:
    return Script

def GetGuild(CTX: Commands.Context) -> None:
    Guild = CTX.guild

    return Guild


# -- SETTERS -- #

async def SetPresence(Activity: Discord.Activity, Status: Discord.Status) -> None:
    await Client.change_presence(activity=Activity,
                                   status=Status)
    
    print(f"{Emojis["Controller"]} Presence set to {Activity.type.name} : Status - {Status}{Newline}")

async def SendGreeting(Member: Discord.Member, Message: str = None, ChannelID: int = None) -> None:
    """

        Try and avoid editing this function, rather edit `./events.py`
    
    """

    GreetingChannel = ChannelID or 1314000162733166623
    Greeting = Message or f"{CustomEmojis["Join"]} Thanks for joining Starry, find the script by using **`/script`**"

    Embed = Discord.Embed(title=f"Thanks for Joining {Whitespace}{Emojis["Wave"]}",
                          description=Greeting,
                          color=Discord.Colour.green())
    
    Channel = Client.get_channel(GreetingChannel)

    if Channel is not None:
        await Channel.send(embed=Embed)

        print(f"{Emojis["Wave"]} {Member.name} has joined the server!")

    else:
        print(f"{Emojis["X"]} Channel not found! - {GreetingChannel}")

async def AssignRole(Member: Discord.Member, Roles: list) -> None:
    for Role in Roles:
        if Role is not None and Role not in Member.roles:
            await Member.add_roles(Role)

            print(f"{Emojis["Book"]} {Member.name} has been assigned the {Role.name} role!")
