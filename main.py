import discord
import os
import requests
import json
import random

os.system('pip install -U coc.py')

import coc
from replit import db
from keep_alive import keep_alive

from discord.ext import commands
from discord.utils import get

intents = discord.Intents().all()
Bot=commands.Bot(command_prefix='^', help_command=None, intents=intents)

def get_quote():
	response=requests.get("https://zenquotes.io/api/random")
	json_data=json.loads(response.text)
	quote=json_data[0]['q'] + "-" + json_data[0]['a']
	return(quote)

@Bot.event
async def on_ready():
	await Bot.change_presence(activity=discord.Game(name="^help"))
	print('We have logged in as {0.user}'.format(Bot))

@Bot.event
async def on_member_join(member):
	guild=Bot.get_guild(682165945032376360)
	lobby=guild.get_channel(749574197386281000) #lobby channel for greeting
	await lobby.send(f'''
Hey {member.mention}, welcome to {guild.name}!
Our clan information is available in <#749574106982383657> .
Pls wait while someone gets in touch with you. Guest roles till then.
Potential Joinees- Post profile ss/ mention TH lvl.
Clan members - Let us know your clan and name for the member role.
IMP- Change you nickname to your In Game Name (IGN). Thanks
''')
	
	pj = discord.utils.get(member.guild.roles, id = 749934681230671910) #Give them `Potential Joinees` role via id
	await member.add_roles(pj)

@Bot.command()
async def ping(ctx):
	await ctx.send(f'Pong ! {round(Bot.latency*1000)} ms')

@Bot.command(aliases=['h'])
async def help(ctx, *params):
	await ctx.channel.send('''
```
^hi - To recieve a greeting
^invite - To invite the bot to your server
^inspire - To get an inspirational quote
^ping - To check if the bot is online
^n - To learn how to change nickname
^fc - Link to join Friendly clan
^a7 - Link to join Assasssin 007
^owner - To know who owns this bot
^fcrole - Admin Command
^a7role - Admin Command
^left - Admin Command
^info <player tag> - To display basic stats of the player
^guess <number> - Guessing Game between 1-10 both inclusive
```
''')

@Bot.command(aliases=['hello'])
async def hi(ctx):
	await ctx.send("Hello!")

@Bot.command()
async def invite(ctx):
	await ctx.send("https://discord.com/api/oauth2/authorize?client_id=834036019795722291&permissions=2416438336&scope=bot")

@Bot.command()
async def inspire(ctx):
	quote=get_quote()
	await ctx.send(quote)

@Bot.command()
async def n(ctx):
	await ctx.send('''
How to change your nickname?\n
PC : 
• Right click on server icon
• Choose 'Change Nickname'
• Type your choice of nickname
• Click 'Save'\n
Device :
• Click on server icon
• Click on three veritical dots 
• Choose 'Change Nickname'
• Type your choice of nickname 
• Click 'Save'
''')

@Bot.command()
async def fc(ctx):
	await ctx.send('''
Clash of Clans : Friendly clan : #8QCY8LJ0
Direct Clash link to open in game: https://link.clashofclans.com/en?action=OpenClanProfile&tag=8QCY8LJ0
''')

@Bot.command()
async def a7(ctx):
	await ctx.send('''Clash of Clans : Assassin 007 : #29CLYLRL0
Direct Clash link to open in game : https://link.clashofclans.com/en?action=OpenClanProfile&tag=29CLYLRL0
''')

@Bot.command()
async def owner(ctx):
	await ctx.send("I am owned by tushar :partying_face:")

@Bot.command()
async def fcrole(ctx, user: discord.Member):
	pj = discord.utils.get(ctx.guild.roles, id=749934681230671910)
	fc = discord.utils.get(ctx.guild.roles, name="Friendly-Clan-Members")
	if ctx.author.guild_permissions.administrator:
		await user.add_roles(fc)
		await user.remove_roles(pj)
		await ctx.send(f"Welcome to Friendly clan!")

@Bot.command()
async def a7role(ctx, user: discord.Member):
	pj = discord.utils.get(ctx.guild.roles, id=749934681230671910)
	a7 = discord.utils.get(ctx.guild.roles, name="Assassin-007-Members")
	if ctx.author.guild_permissions.administrator:
		await user.add_roles(a7)
		await user.remove_roles(pj)
		await ctx.send(f"Welcome to Assassin 007!")

@Bot.command()
async def left(ctx, user: discord.Member):
	pj = discord.utils.get(ctx.guild.roles, id=749934681230671910)
	fc = discord.utils.get(ctx.guild.roles, name="Friendly-Clan-Members")
	a7 = discord.utils.get(ctx.guild.roles, name="Assassin-007-Members")
	if ctx.author.guild_permissions.administrator:
		await user.add_roles(pj)	
		if fc in user.roles:	
			await user.remove_roles(fc)
		if a7 in user.roles:
			await user.remove_roles(a7)
		await ctx.send("Done")

coc=coc.login(os.getenv('email'), os.getenv('password'),client=coc.EventsClient)

@Bot.command()
async def info(ctx, tag):
	player = await coc.get_player(tag)

	e = discord.Embed(colour=discord.Colour.green())
	e.add_field(name="Name", value=player.name, inline=False)
	e.add_field(name="Tag", value=player.tag, inline=False)
	e.add_field(name="TH", value=player.town_hall, inline=False)
	e.add_field(name="Attack Wins", value=player.attack_wins, inline=False)
	for hero in player.heroes:
		e.add_field(name="Heroes", value="{}: Lv {}\n".format(str(hero), hero.level), inline=False)

	await ctx.send(embed=e)

@Bot.command()
async def guess(ctx, n):
  N=random.randint(1,10)
  if int(n)==N:
    await ctx.send("You are one lucky person!!")
  elif int(n)>10:
    await ctx.send("Trying to lose are we?")
  else:
    await ctx.send("10 numbers are a lot...Better luck next time")

keep_alive()
Bot.run(os.getenv('TOKEN'))
 
