import discord as Discord
import dotenv as Env
import os as OS
import asyncio as Async

from constants import *

Env.load_dotenv()

client = Commands.Bot(command_prefix="s.",
                      intents=Discord.Intents.all())

# Events

@client.event
async def on_ready():
    print(f"🚀 Discord Bot ready!")
    print(f"👋 Logged in as {client.user.name} ({client.user.id})")

    await client.change_presence(activity=Discord.Activity(type=Discord.ActivityType.listening),
                                 status=Discord.Status.online)
    
@client.event
async def on_command_error(CTX: Commands.Context, errorCode):
    print(f"❌ An error occurred: {errorCode}")

    pass
    
# Load Commands

for filename in OS.listdir('./commands'):
    if filename.endswith('.py'):
        Async.run(client.load_extension(f'commands.{filename[:-3]}'))
        print(f"📚 Loaded command file: {filename[:-3]}")
    
# Connect Bot

client.run(OS.getenv("TOKEN"))