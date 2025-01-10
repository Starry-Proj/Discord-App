import discord as Discord;
import os      as OS;

from discord.ext import commands as Commands;
from .constants  import *;                       # Load our Constant Variables

"""

    This script is aimed towards GETTER and possible SETTER functions.

    Mainly to just get information though.

    --

    Written: 1/4/2025 - 1/10/2025

"""

# Variables

Client: Commands.Bot = Commands.Bot(command_prefix="$",
                      intents=Discord.Intents.all())

Script: str = f"loadstring(game:HttpGet(\"https://luau.tech/build\"))()"


# -- GENERAL FUNCTIONS -- #

def FormatTime(Minutes: int) -> str:
    TotalSeconds = Minutes * 60

    def Round(Input: int) -> int:
        Rounded = round(Input, 1)

        if Rounded == 0.0:
            return 0

        return Rounded

    Hours = Round((TotalSeconds // 3600) % 24)
    Minutes = Round((TotalSeconds % 3600) // 60)
    Seconds = Round(TotalSeconds % 60)

    return f"{Hours} {"hours" if Hours != 1 else "hour"}, {Minutes} {"minutes" if Minutes != 1 else "minute"} and {Seconds} {"seconds" if Seconds != 1 else "second"}"

def FormatNumber(Number: int) -> str:
    assert isinstance(Number, int), "Number should be of type \"int\""

    """
    
        This function will turn something like 1000 into 1,000.
    
    """

    Formatted = "{:,}".format(Number)

    print(f"{Newline}{Emojis["Book"]} Formatted number: {Formatted}{Newline}")

    return Formatted

def OpenFile(File: str = None, Mode: str = "r") -> str:
    assert isinstance(File, str), "File should be of type \"str\""
    assert isinstance(Mode, str), "Mode should be of type \"str\""

    Content = ""

    for Root, _, Files in OS.walk("."):
        if File in Files:
            Path = OS.path.join(Root, File)

            with open(Path, Mode) as Cached:
                Content = Cached.read()

            break

    return Content

def RemoveCache() -> None:
    for Root, _, Files in OS.walk("."):
        if "__pycache__" in Root:
            for File in Files:
                OS.remove(f"{Root}/{File}")

            OS.rmdir(Root)


# -- UTILITY -- #

def PermissionExists(Permission: str) -> bool:
    return hasattr(Discord.Permissions, Permission)

def AllowedPermissions(Permissions: list) -> list: # e.g. -> AllowedPermissions(["manage_server", "administrator", "moderate_members"])
    FinalList = []

    for Permission in Permissions:
        if PermissionExists(Permission):
            FinalList.append(Permission)

    return FinalList

def IsMuted(Member: Discord.Member) -> bool:
    if Member.timed_out_until:
        return True
    
    return False

def ItemInList(List: list, *Item) -> bool:
    for Item in List:
        if Item in List:
            return True
        
    return False


# -- EMBEDS -- #

def Failure(Issue: str, Command: str, Description: str, Reason: str) -> Discord.Embed:
    MessageBox = f"```md{Newline}# {Reason}{Newline}```"

    Embed: Discord.Embed = Discord.Embed(title=f"{Command}  —  {Issue}",
                                         description=f"{Description}{Newline}{Newline}{MessageBox if Reason != None else ""}",
                                         color=Discord.Color.red())
    
    return Embed


# -- GETTERS -- #

def GetPermissions(Member: Discord.Member) -> list:
    PermList: list = []
    
    for Role in Member.roles:
        if Role.name != "@everyone":
            for Perm in Role.permissions:
                if getattr(Role.permissions, Perm, False):
                    PermList.append(Perm)

    return PermList

def GetClient() -> Commands.Bot:
    return Client

def GetScript() -> str:
    return Script


# -- SETTERS -- #

async def SetPresence(Activity: Discord.Activity, Status: Discord.Status) -> None:
    assert isinstance(Activity, Discord.Activity), "Discord Activity should be of type \"Discord.Activity\""
    assert isinstance(Status, Discord.Status), "Discord Status should be of type \"Discord.Status\""

    await Client.change_presence(activity=Activity,
                                   status=Status)
    
    print(f"{Emojis["Controller"]} Presence set to {Activity.type.name} : Status - {Status}{Newline}")

async def SendGreeting(Member: Discord.Member, Message: str = None, ChannelID: int = None) -> None:
    assert isinstance(Member, Discord.Member), "Discord Member should be of type \"Discord.Member\""
    assert isinstance(Message, str), "Embedded message should be of type \"str\""
    assert isinstance(ChannelID, int), "Channel ID should be of type \"int\""

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
        await Channel.send(content=f"<@{Member.id}>", embed=Embed)

        print(f"{Emojis["Wave"]} {Member.name} has joined the server!")

    else:
        print(f"{Emojis["X"]} Channel not found! - {GreetingChannel}")

async def AssignRole(Member: Discord.Member, Roles: list) -> None:
    assert isinstance(Member, Discord.Member), "Discord Member should be of type \"Discord.Member\""
    assert isinstance(Roles, list), "Roles list should be of type \"list\""

    for Role in Roles:
        if Role is not None and Role not in Member.roles:
            await Member.add_roles(Role)

            print(f"{Emojis["Book"]} {Member.name} has been assigned the {Role.name} role!")
