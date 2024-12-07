import discord as Discord
from discord.ui import Button, View

def formatNumber(number: int) -> str:
    return "{:,}".format(number)

def errorEmbed(overrideColor: Discord.Color = None, title: str = None, description: str = None, footer: str = None, fields: list = None, buttons: list = None) -> Discord.Embed:
    embed = Discord.Embed(title=title if title else None,
                          description=description if description else None,
                          color=overrideColor if overrideColor != None else Discord.Color.red())
    
    if fields:
        for field in fields:  
            embed.add_field(name=field[0],
                            value=field[1],
                            inline=field[2])
            
    if footer:
        embed.set_footer(text=footer)
    
    view = View()
    if buttons:
        for button in buttons:
            btn = Button(label=button['label'], style=button['style'], custom_id=button['custom_id'])
            view.add_item(btn)
        
    return embed 

def successEmbed(overrideColor: Discord.Color = None, title: str = None, description: str = None, footer: str = None, fields: list = None, buttons: list = None) -> Discord.Embed:
    embed = Discord.Embed(title=title if title else None,
                          description=description if description else None,
                          color=overrideColor if overrideColor != None else Discord.Color.green())
    
    if fields:
        for field in fields:  
            embed.add_field(name=field[0],
                            value=field[1],
                            inline=field[2])
        
    if footer:
        embed.set_footer(text=footer)
    
    view = View()
    if buttons:
        for button in buttons:
            btn = Button(label=button['label'], style=button['style'], custom_id=button['custom_id'])
            view.add_item(btn)
        
    return embed
