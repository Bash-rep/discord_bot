import os
import asyncio
import random
import discord

TOKEN = 'Njk0NTU5NTk0ODA1OTg1NDAz.XouLxg.TEZF4nns4DHQ1-9oH1iC-uFswVc'
GUILD = '631950256065609739'
client = discord.Client()


@client.event
async def on_ready():
	print(f'{client.user} has connected to Discord')
	print(f'{client.guilds} has connected to Discord')

	for guild in client.guilds:
		if guild.name == GUILD:
			break
	
	print(
	f'{client.user} is connected to the following guild:\n'
	f'{guild.name}(id: {guild.id})'
	)

	members = '\n - '.join([member.name for member in guild.members])
	print(f'Guild Members:\n - {members}')

@client.event
async def on_message(message):
	if message.author == client.user:
		return

	for guild in client.guilds:
		if guild.name == GUILD:
			break

	if 'beep-boop-bot' in str(message.channel):
		if message.content.lower().replace(' ','') == 'quememalandro?':
			response = rnd_name(guild)
			await message.channel.send('@'+response)
		if message.content == 'f':
			await message.channel.send('Leave your F\'s in the chat bois')
			await message.channel.send(file=discord.File('my_image.png'))
		if message.content == 'yay':
			play_this(message.author, 'yay.mp3')


async def play_this(user, audioFile): 
	vc = await user.voice.channel.connect()
	vc.play(discord.FFmpegPCMAudio('yay.mp3'), after=lambda e: print('done', e))
	while vc.is_playing():
		await asyncio.sleep(1)
	vc.stop()
	await vc.disconnect()

def rnd_name(guild):
	members = []
	members.append([member.name for member in guild.members])
	return members[0][random.randint(0,len(members[0])-1)]


client.run(TOKEN)
