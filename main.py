import discord as Discord
import os as OS
import asyncio as Async

from modules.functions import *
from constants import *

# Events

@client.event
async def on_ready():
    print(f"🚀 Discord Bot ready!")
    print(f"👋 Logged in as {client.user.name} ({client.user.id})")

    await client.change_presence(activity=Discord.Activity(type=Discord.ActivityType.listening, name="/script"),
                                 status=Discord.Status.online)
    
@client.event
async def on_command_error(CTX: Commands.Context, errorCode):
    print(f"❌ An error occurred: {errorCode}")

    pass

@client.event
async def on_member_join(member: Discord.Member):
   print(f"👋 Member {member.name} joined the server!")
   memberRole = 1314031703324495902
   ogRole = 1258791001041014857 
   welcomeChannel = 1317785239879286786
   guild = member.guild
   isOg = False if guild.member_count > 1000 else True
   
   try:
       # Add roles
       await member.add_roles(guild.get_role(memberRole))
       if isOg:
           await member.add_roles(guild.get_role(ogRole))
           
       channel = guild.get_channel(welcomeChannel)
       if channel:
           welcome_embed = Discord.Embed(
    color=0x43b47e,
    description=f"> <:discordjoin:1267648662952214571> <@{member.id}> has joined the server!"
)   
           await channel.send(embed=welcome_embed)
   except:
       pass
      
   await member.send(content=f"<@{member.id}>", embed=successEmbed(Discord.Color.green(),
                                                                   f"Welcome to Starry",
                                                                   "We appreciate you joining our server and supporting us in the process!\n- Support future development and feel free to **boost our server**!",
                                                                   "Made with ❤️ by the Starry Team",
                                                                   fields=[
                                                                       ["Invite", "- [disсord.gg/zyXZSn97hN](https://discord.gg/zyXZSn97hN)", False],
                                                                   ]))
# Load Commands

for filename in OS.listdir('./commands'):
    if filename.endswith('.py'):
        Async.run(client.load_extension(f'commands.{filename[:-3]}'))
        print(f"📚 Loaded command file: {filename[:-3]}")
    
# Connect Bot

client.run("discord.gg/luau")