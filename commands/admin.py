import time as Time;

from discord.ext      import commands as Commands;
from assets.functions import *;                     # Load our Functions
from assets.constants import *;                     # Load our Constant Variables
from datetime         import timedelta;

"""

    This file handles ALL free-to-use commands, here's a list:

    - ban <member> <reason>     - Bans a member from the server
    - kick <member> <reason>    - Kicks a member from the server
    - mute <member> <reason>    - Mutes a member in the server
    - unmute <member>           - Unmutes a member in the server
    - clear <amount>            - Clears a certain amount of messages in the channel

    --

    Written: 1/8/2025

    P.S.: I'm SO sorry for this file being coded horribly.. I tried my best to make it nice

"""

class Admin(Commands.Cog):
    def __init__(self, App) -> None:
        self.App = App

    # Commands

    # -- Ban / Kick / Unban Commands -- #

    @Commands.cooldown(1, 5, Commands.BucketType.user)
    @Commands.hybrid_command(name="ban",
                             description=f"{Emojis["Lock"]} Forever remove a member* from the server")
    
    async def Ban(self, CTX: Commands.Context, member: Discord.Member, reason: str = None) -> None:
        Guild: Discord.Guild = CTX.guild
        BanReason: str = reason or "Unspecified"
        Self: Discord.Member = CTX.author

        if not ItemInList(GetPermissions(Self), "ban_members", "administrator", "manage_server"):
            return await CTX.reply(content=f"<@{Self.id}>", embed=Failure("Missing Permission", "Ban", "You're missing permissions to use this command", "Missing either Ban Members, Manage Server, or Administrator"))

        if not Guild:
            return await CTX.reply(content=f"<@{Self.id}> {Newline}## Out of Server.. {Newline} This command can only be used in a server, {Newline}- we advise you join our official [Discord server](https://discord.gg/luau) @ discord.gg/luau {Newline}{Whitespace}")

        if not member or member == None:
            return await CTX.reply(embed=Failure("Missing param.", "Ban", "Command failed due to a missing parameter", "Missing \"Member\" parameter"), ephemeral=True, delete_after=10)
        
        Embed = Discord.Embed(title="Member Banned",
                              description=f"<@{member.id}>{Whitespace} has been permanently banned",
                              color=Discord.Color.green())
        
        Embed.add_field(name="Server", value=Guild.name)
        
        if BanReason != "Unspecified":
            Embed.add_field(name="Reason", value=BanReason)

        await member.ban(reason=BanReason, delete_message_days=7)
        await CTX.reply(embed=Embed, delete_after=10)

    @Commands.cooldown(1, 5, Commands.BucketType.user)
    @Commands.hybrid_command(name="unban",
                             description=f"{Emojis["Lock"]} Allows an already banned member to join back")
    
    async def Unban(self, CTX: Commands.Context, user_id: int) -> None:
        Guild: Discord.Guild = CTX.guild
        Self: Discord.Member = CTX.author

        if not ItemInList(GetPermissions(Self), "ban_members", "administrator", "manage_server"):
            return await CTX.reply(content=f"<@{Self.id}>", embed=Failure("Missing Permission", "Unban", "You're missing permissions to use this command", "Missing either Ban Members, Manage Server, or Administrator"))

    
    @Commands.cooldown(1, 5, Commands.BucketType.user)
    @Commands.hybrid_command(name="kick",
                             description=f"{Emojis["Lock"]} Remove a member* from the server")
    
    async def Kick(self, CTX: Commands.Context, member: Discord.Member, reason: str = None) -> None:
        Guild: Discord.Guild = CTX.guild
        KickReason: str = reason or "Unspecified"
        Self: Discord.Member = CTX.author

        if not ItemInList(GetPermissions(Self), "kick_members", "administrator", "manage_server"):
            return await CTX.reply(content=f"<@{Self.id}>", embed=Failure("Missing Permission", "Kick", "You're missing permissions to use this command", "Missing either Kick Members, Manage Server, or Administrator"))

        if not Guild:
            return await CTX.reply(content=f"<@{Self.id}> {Newline}## Out of Server.. {Newline} This command can only be used in a server, {Newline}- we advise you join our official [Discord server](https://discord.gg/luau) @ discord.gg/luau {Newline}{Whitespace}")

        if not member or member == None:
            return await CTX.reply(embed=Failure("Missing param.", "Kick", "Command failed due to a missing parameter", "Missing \"Member\" parameter"), ephemeral=True, delete_after=10)

        Embed = Discord.Embed(title="Member Removed",
                              description=f"<@{member.id}>{Whitespace} was kicked from **{Guild.name}**",
                              color=Discord.Color.green())
        
        Embed.add_field(name="Server", value=Guild.name)
        
        if KickReason != "Unspecified":
            Embed.add_field(name="Reason", value=KickReason)

        await member.kick(reason=KickReason)
        await CTX.reply(embed=Embed, delete_after=10)


    # -- Mute / Unmute Commands -- #

    @Commands.cooldown(1, 5, Commands.BucketType.user)
    @Commands.hybrid_command(name="mute",
                             description=f"{Emojis["Lock"]} Mute a member* for a certain amount of time")
    
    async def Mute(self, CTX: Commands.Context, member: Discord.Member, minutes: int = None, reason: str = None) -> None:
        Guild = CTX.guild
        MuteReason = reason or "Unspecified"
        Self: Discord.Member = CTX.author

        if not ItemInList(GetPermissions(Self), "manage_members", "administrator", "manage_server"):
            return await CTX.reply(content=f"<@{Self.id}>", embed=Failure("Missing Permission", "Mute", "You're missing permissions to use this command", "Missing either Manage Members, Manage Server, or Administrator"))

        if not Guild:
            return await CTX.reply(content=f"<@{Self.id}> {Newline}## Out of Server.. {Newline} This command can only be used in a server, {Newline}- we advise you join our official [Discord server](https://discord.gg/luau) @ discord.gg/luau {Newline}{Whitespace}")
        
        if not member or member == None:
            return await CTX.reply(embed=Failure("Missing param.", "Mute", "Command failed due to a missing parameter", "Missing \"Member\" parameter"), ephemeral=True, delete_after=10)

        if IsMuted(member):
            await member.timeout(None)

        Embed = Discord.Embed(title="Muted Member",
                              description=f"<@{member.id}>{Whitespace} has been timed out, {Newline}- They're now unable to chat, react, or join voice calls",
                              color=Discord.Color.teal())
        
        Embed.add_field(name="Duration", value=FormatTime(minutes), inline=True)

        if MuteReason != "Unspecified":
            Embed.add_field(name="Reason", value=MuteReason, inline=True)

        await member.timeout(timedelta(minutes=minutes))
        await CTX.reply(embed=Embed, delete_after=10)


    @Commands.cooldown(1, 5, Commands.BucketType.user)
    @Commands.hybrid_command(name="unmute",
                             description=f"{Emojis["Lock"]} Remove a member's timeout")
    
    async def Unmute(self, CTX: Commands.Context, member: Discord.Member) -> None:
        Guild = CTX.guild
        Self: Discord.Member = CTX.author

        if not ItemInList(GetPermissions(Self), "manage_members", "administrator", "manage_server"):
            return await CTX.reply(content=f"<@{Self.id}>", embed=Failure("Missing Permission", "Unmute", "You're missing permissions to use this command", "Missing either Manage Members, Manage Server, or Administrator"))

        if not Guild:
            return await CTX.reply(content=f"<@{Self.id}> {Newline}## Out of Server.. {Newline} This command can only be used in a server, {Newline}- we advise you join our official [Discord server](https://discord.gg/luau) @ discord.gg/luau {Newline}{Whitespace}")

        if not member or member == None:
            return await CTX.reply(embed=Failure("Missing param.", "Unmute", "Command failed due to a missing parameter", "Missing \"Member\" parameter"), ephemeral=True, delete_after=10)

        if not IsMuted(member):
            return await CTX.reply(embed=Failure("Timeout Failure", "Unmute", "Could not unmute a member that has not been muted", Reason=None))

        Embed = Discord.Embed(title="Member Timeout Removed",
                              description=f"Removed timeout from {Whitespace}<@{member.id}>",
                              color=Discord.Color.teal())
        
        await member.timeout(None)
        await CTX.reply(embed=Embed, delete_after=10)


    # -- Clear Command -- #

    @Commands.cooldown(1, 5, Commands.BucketType.user)
    @Commands.hybrid_command(name="clear",
                             description=f"{Emojis["Lock"]} Quickly delete messages in bulk",
                             aliases=["purge", "clean"])
    
    async def Clear(self, CTX: Commands.Context, messages: int = None, channel: Discord.TextChannel = None) -> None:
        Guild = CTX.guild
        Member = CTX.author
        Self: Discord.Member = CTX.author

        if not ItemInList(GetPermissions(Self), "manage_messages", "administrator", "manage_server"):
            return await CTX.reply(content=f"<@{Self.id}>", embed=Failure("Missing Permission", "Clear", "You're missing permissions to use this command", "Missing either Manage Messages, Manage Server, or Administrator"))

        if not Guild:
            return await CTX.reply(content=f"<@{Self.id}> {Newline}## Out of Server.. {Newline} This command can only be used in a server, {Newline}- we advise you join our official [Discord server](https://discord.gg/luau) @ discord.gg/luau {Newline}{Whitespace}")

        if not channel or channel == None:
            channel = CTX.channel

        if not messages or messages == None:
            messages = 64

        Plural = "messages" if messages != 1 else "message"

        await CTX.reply(content=f"Please wait while I purge up to {messages} {Plural}..", delete_after=5)

        Starting = Time.time()

        Time.sleep(1)

        await channel.purge(limit=messages + 1) # Cleanse a channel

        Ending = Time.time()
        Duration = (Ending - Starting) / 60

        Embed = Discord.Embed(title="Message Purge",
                              description="Finished the message cleanse, here's what you should know",
                              color=Discord.Color.blurple())
        
        Embed.add_field(name="Message Count", value=messages, inline=True)
        Embed.add_field(name="Duration", value=FormatTime(Duration))

        await CTX.send(content=f"<@{Member.id}>", embed=Embed, delete_after=10)


# -- Setup the Cog -- #

async def setup(App) -> None:
    await App.add_cog(Admin(App))
