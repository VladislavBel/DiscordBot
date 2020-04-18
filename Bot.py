import discord
import time
import asyncio


def read_token():
    with open('token', 'r') as f:
        lines = f.readlines()
        return lines[0].strip()


token = read_token()
client = discord.Client()

messages = joined = 0
id = client.get_guild(701085066687938621)


async def update_status():

    await client.wait_until_ready()
    global messages, joined

    while not client.is_closed():
        try:
            with open('stats', 'a') as f:
                f.write(f"Time: {int(time.time())}, Messages: {messages}, members joined: {joined}\n")

            messages = 0
            joined = 0

            await asyncio.sleep(5)
        except Exception as e:
            print(e)
            await asyncio.sleep(5)



@client.event
async def on_member_join(member):
    global joined
    joined += 1
    for channel in member.server.channels:
        if str(channel) == 'general':
            await client.send_message(f"""Hello fellow degenerate {member.mention}""")


@client.event
async def on_message(message):

    global messages
    messages += 1

    if message.content.find('!hello') != -1:
        await message.channel.send('Howdy')

    elif message.content == ('!users'):
        await message.channel.send(f"""Num of members {id.member_count}""")

client.loop.create_task(update_status())
client.run(token)