import discord as Discord;

from discord.ext import commands as Commands;
from .functions  import *;                       # Load our Functions
from .constants  import *;                       # Load our Constant Variables

"""

    This script is our Event Handler,
    
    & it's used to handle all sorts of events, e.g. on_ready, on_member_join, etc.

    --

    Written: 1/4/2025

"""

# Variables

Client  = GetClient()


# Event Handling

def SetupEvents() -> None:
    @Client.event
    async def on_ready() -> None:
        print(f"{Newline}{Emojis["Rocket"]} Discord Bot ready!")
        print(f"{Emojis["Wave"]} Logged in as {Client.user.name} : UID - {Client.user.id}{Newline}")

        RemoveCache()


    @Client.event
    async def on_member_join(Member: Discord.Member) -> None:
        MembersRole = Discord.utils.get(Member.guild.roles, id=1314112853942472735)
        ScriptChannel = Client.get_channel(1314061731114389574)

        if not ScriptChannel:
            ScriptChannel = "<#1314061731114389574>"

        JoinMessage = f"{CustomEmojis["Join"]} Thank you, <@{Member.id}> for joining Starry! {Newline}- Find the latest script in {ScriptChannel}"

        await SendGreeting(Member, JoinMessage, 1314000162733166623)
        await AssignRole(Member, [MembersRole])
