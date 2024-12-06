import discord as Discord;

from discord.ext import commands as Commands;


# Constants

client = Commands.Bot(command_prefix="s.",
                      intents=Discord.Intents.all())