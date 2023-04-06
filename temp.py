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
    print("Money!")
    print("------")

@client.command()
async def hello(ctx):
    await ctx.send("Hello, give your money!")

@client.command()
async def bankclosed(ctx):
    await ctx.send("Bye, remember to make money.")

@client.event
async def on_member_join(member):
    channel = client.get_channel(708364225323728978)
    await channel.send("Another slave here!")

@client.command(pass_context = True)
async def call(ctx):
    if (ctx.author.voice):
        channel = ctx.message.author.voice.channel
        await channel.connect()
    else:
        await ctx.send("今日休市")

@client.command(pass_context = True)
async def put(ctx):
    if (ctx.voice_client):
        await ctx.guild.voice_client.disconnect()
        await ctx.send("休市時段")
    else:
        await ctx.send("休市")

@client.command()
async def embed(ctx):
    embed = nextcord.Embed(title="Dog", url="https://google.com", description="We love dogs!", color=0x4dff4d)
    embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar.url)
    embed.set_thumbnail(url="https://na.cx/i/WPOptGR.png")
    embed.add_field(name="Labradore", value="This is a test field", inline=True)
    embed.add_field(name="Pugs", value="Cute dogs", inline=True)
    embed.set_footer(text="Thank you for reading")
    await ctx.send(embed=embed)

@client.command()
async def direct(ctx):
    message = "Welcome to the server!"
    embed = nextcord.Embed(title=message)
    await ctx.author.send(embed=embed)

testServerId = 708364224702841028

@nextcord.slash_command(name = "test", description = "Introduction to Slash Commands", guild_ids=[testServerId])
async def test(self, interaction: Interaction):
    await interaction.response.send_message("Hello, gogo")
        
@client.slash_command(name = "repeat", description = "tts", guild_ids=[testServerId])
async def repeat(interaction: Interaction, message:str):
    await interaction.response.send_message(f"you said `{message}`")


intitial_extensions = [] # array that get all the cog

for filename in os.listdir('Z:\main\DataCenter\Python_code\Discord-Project\cogs'):
    if filename.endswith('.py'):
        intitial_extensions.append("cogs." + filename[:-3])

if __name__ == '__main__':
    for extension in intitial_extensions:
        client.load_extension(extension)


client.run(TOKEN)



