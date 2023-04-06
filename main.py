import nextcord
from nextcord import Interaction
from nextcord.ext import commands
import os

from apikeys import *

intents = nextcord.Intents.all()
intents.members = True

client = commands.Bot(command_prefix='$', intents=intents)
prefix = "$"


@client.event
async def on_ready():
    print("Ready")
    master = await client.fetch_user(admin)
    await master.send("Ready")
    await master.send("打 $gameb 開始遊戲")

intitial_extensions = [] # array that get all the cog

for filename in os.listdir('Z:\main\DataCenter\Python_code\Discord-Project\cogs'):
    if filename.endswith('.py'):
        intitial_extensions.append("cogs." + filename[:-3])

if __name__ == '__main__':
    for extension in intitial_extensions:
        client.load_extension(extension)

client.run(TOKEN)
