import nextcord
from nextcord import Interaction
from nextcord.ext import commands

class Greetings(commands.Cog):

    def __init__(self,client):
        self.client = client
    
    @commands.command()
    async def hello(self, ctx):
        await ctx.send("Hello, give your money!")

    @commands.command()
    async def bankclosed(self, ctx):
        await ctx.send("Bye, remember to make money.")
    
    @commands.command(pass_context = True)
    async def call(self, ctx):
        if (ctx.author.voice):
            channel = ctx.message.author.voice.channel
            await channel.connect()
        else:
            await ctx.send("今日休市")

    @commands.command(pass_context = True)
    async def put(self, ctx):
        if (ctx.voice_client):
            await ctx.guild.voice_client.disconnect()
            await ctx.send("休市時段")
        else:
            await ctx.send("休市")
    
def setup(client):
    client.add_cog(Greetings(client))