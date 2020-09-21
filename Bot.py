import discord
import time
import asyncio
from ChatAI import chat


def read_token():
    with open('token', 'r') as f:
        lines = f.readlines()
        return lines[0].strip()


token = read_token()
client = discord.Client()

messages = joined = 0


async def update_status():

    await client.wait_until_ready()
    global messages, joined

    while not client.is_closed():
        try:
            with open('stats', 'a') as f:
                f.write(f"Time: {int(time.time())}, Messages: {messages}, members joined: {joined}\n")

            messages = 0
            joined = 0

            await asyncio.sleep(3600)
        except Exception as e:
            print(e)
            await asyncio.sleep(3600)



@client.event
async def on_member_join(member):
    global joined
    joined += 1
    guild_id = client.get_guild(701085066687938621)
    welcomes = guild_id.get_channel(701085066687938625)
    await welcomes.send(f"""Hello fellow degenerate {member.mention}""")


@client.event
async def on_message(message):

    global messages
    messages += 1
    guild_id = client.get_guild(701085066687938621)

    if message.content.find('Akagi hello') != -1:
        await message.channel.send('Ah skikahhhhh.... I was waiting for you')

    elif message.content == ('Akagi users'):

        await message.channel.send(f"""Num of members {guild_id.member_count}""")

    elif message.content == ('Akagi members status'):

        members = set(client.get_all_members())
        mem_status = {'online': 0, 'idle': 0, 'do not disturb': 0, 'offline': 0}
        
        for member in members:
            mem_status[str(member.status)] += 1
        await message.channel.send(f"""Online: {mem_status['online']},\nIdle/DND: {mem_status['idle']}/{mem_status['do not disturb']},\nOffline: {mem_status['offline']}.""")

    elif message.content == ('Akagi chat'):

        chat()

client.loop.create_task(update_status())
client.run(token)