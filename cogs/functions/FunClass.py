import nextcord
from nextcord.ext import commands
from nextcord import Interaction
import asyncio
import sqlite3 as sl

def isfloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False

async def checnkbalance(x, dm_channel, balance):
    if x == 0:   
        if balance >= 0:
            await dm_channel.send("閣下的資產已被涷結，結餘： $" + str(balance))
        else:
            await dm_channel.send("閣下的資產已被涷結，欠餘： $" + str(balance*-1))
    else:
        if balance >= 0:
            await dm_channel.send("注意你還有結餘： $" + str(balance))
        else:
            await dm_channel.send("注意你還有欠餘： $" + str(balance*-1))

async def cushin(self, sent, ctx, user_id, dm_channel):

    conn = sl.connect('cy_bank.db')
    c = conn.cursor()

    try:
        input = await self.client.wait_for(
            "message",
            timeout=60,
            check=lambda message: message.author == ctx.author
        )

        amount = input.content

        if input and isfloat(str(amount)):
            await sent.delete()

            amount = round(float(input.content), 2)

            if amount > 0 and amount <= 3000:

                loading = await ctx.send("入緊awwa")
                c.execute("INSERT INTO TRAN (id,date,type,amount) VALUES (" + user_id + ", date('now'), 0, " + str(amount) + ")")
                c.execute("UPDATE USER SET balance = balance + " + str(amount) + " WHERE id = " + user_id)
                conn.commit()

                await loading.delete()
                await ctx.send("入左 $" + str(amount))
                c.execute("SELECT balance FROM USER WHERE id = " + user_id + ";")
                balance = round(c.fetchone()[0], 2)
                await dm_channel.send("最新結餘： $" + str(balance))

            else:
                await sent.delete()
                await ctx.send("挽野啊on9仔，已扣除10%手續費", delete_after=10)

        else:
            await sent.delete()
            await ctx.send("挽野啊屌你，已扣除10%手續費", delete_after=10)

    except asyncio.TimeoutError:
        await ctx.send("揼波鐘，已自動取消", delete_after=10)

    except ValueError:
        await ctx.send("挽野啊屌你，已扣除10%手續費", delete_after=10)

    except:
        await ctx.send("已扣除$5手續費", delete_after=10)

    c.close()

