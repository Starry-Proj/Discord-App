import discord as Discord;

from discord.ext import commands as Commands;


# Constants

client = Commands.Bot(command_prefix="s.",
                      intents=Discord.Intents.all())

backticks = "```"
script = "getgenv().ignoreGameCheck = false\nloadstring(game:HttpGet(\"https://luau.tech/build\"))()"