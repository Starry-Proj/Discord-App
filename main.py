import discord as Discord
import os      as OS
import asyncio as Async
from fastapi import FastAPI, BackgroundTasks  # Added for web server
import uvicorn                               # Added for web server
from dotenv           import load_dotenv
from assets.functions import *
from assets.events    import *
from assets.errors    import *

# Initialize FastAPI (new)
app = FastAPI()

load_dotenv()

# Variables
TOKEN: str = OS.getenv("TOKEN")
DEVELOPER_TOKEN: str = OS.getenv("DEVELOPER_TOKEN")
Client: Commands.Bot = GetClient()

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
    Description: str = OpenFile("sync.md", "r")
    Embed: Discord.Embed = Discord.Embed(title="Synced Commands",
                          description=Description,
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
SetupEvents()
ErrorHandling()

# -- FastAPI Routes  -- #
@app.get("/")
async def root():
    return {"status": "Bot is running"}

@app.get("/health")
async def health_check():
    return {
        "status": "healthy",
        "bot_latency": round(Client.latency * 1000) if Client.is_ready() else None,
        "guilds_count": len(Client.guilds) if Client.is_ready() else 0
    }

# -- Run both FastAPI and Discord Bot -- #
async def run_bot():
    try:
        await Client.start(TOKEN)
    except Exception as e:
        print(f"Error starting bot: {e}")
    finally:
        print(f"{Newline}{Emojis["X"]} Starry closed & App is offline {Newline}")

async def run_web():
    config = uvicorn.Config(app, host="0.0.0.0", port=8000, loop="asyncio")
    server = uvicorn.Server(config)
    await server.serve()

async def run_all():
    await Async.gather(
        run_bot(),
        run_web()
    )

if __name__ == "__main__":
    Async.run(run_all())