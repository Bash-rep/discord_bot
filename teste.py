import os
import asyncio

import discord

TOKEN = 'Njk0NTU5NTk0ODA1OTg1NDAz.XojZkw.zOOhRnWIZ0AFqUJJvr0g342wuyw'
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
	if message.content == 'yay':
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


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    for guild in client.guilds:
        if guild.name == DISCORD_GUILD:
            break

    members = []
    members.append([member.name for member in guild.members])
    if 'beep-boop-bot' in str(message.channel):
        if message.content.lower().replace(' ','') == 'quememalandro?':
            response = members[0][random.randint(0,len(members[0])-1)]
            await message.channel.send('@'+response)

        if message.content == 'f':
            await message.channel.send('RESPECT')

        if message.content.lower().replace(' ','') == 'yay':
            await message.channel.send('-play https://www.youtube.com/watch?v=attUrDwfdr8')
            time.sleep(10)
            await message.channel.send('-leave')

client.run(TOKEN)
