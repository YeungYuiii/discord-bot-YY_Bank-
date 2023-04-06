import nextcord
from nextcord import Interaction
from nextcord.ext import commands
import sqlite3 as sl

from .functions.Button import *
from .functions.FunClass import *

class Bank(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def calling(self, ctx):
        view = Callings()
        welcome = await ctx.send("歡迎使用宗叡銀行，想點？", view=view)
        await view.wait()
        await welcome.delete()

        conn = sl.connect('cy_bank.db')
        c = conn.cursor()

        user_id = str(ctx.author.id)
        dm_channel = ctx.author.dm_channel

        c.execute("SELECT balance FROM USER WHERE id = " + user_id + ";")
        balance = round(c.fetchone()[0], 2)

        c.close

        if view.value == 0:
            return

        elif view.value == 1:

            await checnkbalance(0, dm_channel, balance)

        elif view.value == 2:

            await checnkbalance(1, dm_channel, balance)
            sent = await ctx.send("想入幾多？請輸入")
            await cushin(self, sent, ctx, user_id, dm_channel)

        elif view.value == 3:
            
            if balance >= 0:
                await ctx.send("注意你還有結餘： $" + str(balance))
            else:
                await ctx.send("注意你還有欠餘： $" + str(balance*-1))

            sent = await ctx.send("想借幾多？請輸入")

    

def setup(client):
    client.add_cog(Bank(client))