import discord
import random
import time
import asyncio
from discord.ext import commands

bot = commands.Bot(command_prefix= '>')

@bot.command(pass_context=True)
async def role(ctx):
	if ctx = message.author
		user = message.author
		for member.roles:
			if role.name != "<role name>":
				await bot.say("Requesting promotion. Please wait for approval")
				for role.name(<moderator>)
					await client.send_message(channel.privat_mod_room, content=user "is requesting the <role name> role", *, tts=False, embed=None)
			else await bot.say("You are already a <role>!")

@bot.command(pass_context=True)
@checks.admin_or_permissions(manage_roles=True)
async def role(ctx, user, yorn):
	if setmemb = ctx:
		if yorn = yes:
			add_roles(user, <role>)
			await client.send_message(user, content="Your request for <role name> has been granted!", *, tts=False, embed=None)
		elif yorn = no:
			await client.send_message(user, content="Sorry, but your request for <role name> has been denied.", *, tts=False, embed=None)
	
@bot.command(pass_context=True)
async def message(ctx):
	if ctx == rmeme:
		await client.send_message(message.channel, content="Wow, a random meme appeared from */r/memes*!", *, tts=False, embed="www.reddit.com/r/memes/random")
        if ctx == rrandom:
		await client.send_message(message.channel, content="Get your daily dose of internet with a random *clean* post from Reddit!", *, tts=False, embed="www.reddit.com/random")
        if ctx == rall:
		await client.send_message(message.channel, content="Find your thing with recent top *clean* posts from **all** of Reddit!", *, tts=False, embed="www.reddit.com/random")
        if ctx == r:
		await bot.say("``````")
         
		
@bot.command(pass_context=True)
@checks.admin_or_permissions(manage_server=True)
async def message(ctx):
	while state == on:
		await client.send_message(channel.memes, content=None, *, tts=False, embed="www.reddit.com/r/memes/random")
	if ctx=memes:
		if state == on:
			state=off
		if state == off:
			state=on
		
@bot.command(pass_context=True)
@checks.admin_or_permissions(mute_user=True)
async def mute(ctx, user, hrs):
	hrs * 3600 = t
	while t	> 0:
		if t > 0:
			await asyncio.sleep(1)
			t = t - 1
	while t > 0:
		if message.author == user:
			await client.delete_message(message)
	await client.send_message(report, content=`***user*** **"was temporarily silenced for" x "hours"**`, *, tts=False, embed=None)

bot.run("<token>")

#make sure to run in a terminal using the latest python while connected to the internet, or the bot will not be online
