import discord as Discord;

from discord.ext      import commands as Commands;
from assets.functions import *;                     # Load our Functions
from assets.constants import *;                     # Load our Constant Variables

"""

    This file handles ALL debug commands, here's a list:

    - ping - Returns the bot's latency
    - test - Does a full permissions check on the bot

    --

    Written: 1/4/2025

"""

class Debug(Commands.Cog):
    def __init__(self, App) -> None:
        self.App = App

    # Commands

    # -- Ping Command -- #

    @Commands.cooldown(1, 5, Commands.BucketType.user)
    @Commands.hybrid_command(name       ="ping",
                             description="Returns Starry's latency in milliseconds")
    
    async def Ping(self, CTX: Commands.Context) -> None:
        """
        
            This command will return a full embed of the everything you'll wanna know,

            e.g. Latency, API Latency, etc.
        
        """

        Ping = round(self.App.latency, 2)

        HasGood = Ping < 100
        IsGood = "fast" if HasGood else "slow"
        Color = Discord.Color.green() if HasGood else Discord.Color.yellow()

        Embed = Discord.Embed(title=f"Pong! {Whitespace}{Emojis["Paddle"]}",
                                description=f"Starry's ping is generally {IsGood} & took **{Ping}** seconds to respond.",
                                color=Color)

        await CTX.reply(embed=Embed, delete_after=10)


    # -- Exam Command -- #

    @Commands.cooldown(1, 5, Commands.BucketType.user)
    @Commands.hybrid_command(name       ="test",
                             description="Does a full permissions check on the bot")
    
    async def Exam(self, CTX: Commands.Context) -> None:
        Guild = CTX.guild

        if not Guild:
            return await CTX.reply(f"<@{CTX.author.id}> {Newline}## Out of Server.. {Newline} This command can only be used in a server, {Newline}- we advise you join our official [Discord server](https://discord.gg/luau) @ discord.gg/luau {Newline}{Whitespace}")

        """
        
            This command should not be used regularly, as it's mainly for debugging purposes.

            After usage, the commands will be forced to wait 30s before using it again.

            This is to prevent a **ton** of Rate Limits to the Discord API

        """

        ManagerPermissions = ["manage_server", "manage_roles", "manage_channels", "manage_nicknames", "manage_webhooks", "manage_messages", "manage_threads", "manage_messages"]
        MembersPermissions = ["kick_members", "ban_members", "moderate_members"]
        UncategorizedPerms = ["create_instant_invite", "create_public_threads", "create_private_threads", "embed_links", "attach_files", "read_message_history", "mention_everyone", "add_reactions"]

        ID    = Guild.me.id

        if ID is None:
            print(f"{Emojis["X"]} Uh oh: Could not find the App's ID")

        def HasPermission(Permission: Discord.Permissions) -> bool:
            Member = Guild.get_member(ID)

            if Member:
                return getattr(Member.guild_permissions, Permission, False)
            
            print(f"{Emojis["X"]} Uh oh: Could not find the App's Member Object")

            return False
        
        FullPermissions = [ManagerPermissions, MembersPermissions, UncategorizedPerms]

        Tested = []

        Percentage = 0
        Failed = 0
        Score = 0

        Highest = len(ManagerPermissions) + len(MembersPermissions) + len(UncategorizedPerms)

        for Permission in FullPermissions:
            for Perm in Permission:
                if HasPermission(Perm):
                    Score += 1
                    Percentage = round((Score / Highest) * 100, 2)

                    Tested.append(Emojis["Check"] + Whitespace + Perm)
                    
                else:
                    Failed += 1

                    Tested.append(Emojis["X"] + Whitespace + Perm)

        Embed = Discord.Embed(title="Permissions Exam",
                              description=f"The exam has finished, with a grade of {Score}/{Highest} ({Failed} Failed) ({Percentage}%)",
                              color=Discord.Color.green())
        
        Embed.add_field(name="Results", value=f"```{Newline.join(Tested)}```")

        await CTX.reply(embed=Embed, delete_after=10)


# -- Setup the Cog -- #

async def setup(App) -> None:
    await App.add_cog(Debug(App))
