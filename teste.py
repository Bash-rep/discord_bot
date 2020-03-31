import os

import discord

TOKEN = 'Njk0MjU5MDA5MDYxOTEyNjQ3.XoJBoA.AAl7ZHPAspaR-XD7HyxZRiuILjo'
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
	if message.content == 'f':
		await message.channel.send(file=discord.File('my_image.png'))
	if message.content == 'yey':
		user = message.author
		vc = await user.voice.channel.connect()
		vc.play(discord.FFmpegPCMAudio('yay.mp3'), after=lambda e: print('done', e))
		#vc.is_playing()
		#vc.pause()
		#vc.resume()
		while vc.is_playing():
			await asyncio.sleep(1)
		vc.stop()
		await vc.disconnect()

client.run(TOKEN)