import nextcord
from nextcord.ext import commands
from nextcord import Interaction
import sqlite3 as sl
import datetime as dt
import random


check_list = ["紅色", "綠色", "紫色", "灰色", "白色", "藍色", "黃色", "黑色", "緣色", "青色", "彩色", "色色", "無色"]
color_list = [nextcord.ButtonStyle.blurple, nextcord.ButtonStyle.grey, nextcord.ButtonStyle.green, nextcord.ButtonStyle.red]
dict = {"藍色": nextcord.ButtonStyle.blurple,
        "灰色": nextcord.ButtonStyle.grey,
        "綠色": nextcord.ButtonStyle.green,
        "紅色": nextcord.ButtonStyle.red
        }

round_check = random.sample(check_list, k=4)

def round_ans():
    
    global round_check
    global color_list
    global ans
    check_list = ["紅色", "綠色", "藍色", "灰色"]
    ans_list = ["紅色", "綠色", "藍色", "灰色"]

    ans = random.choice(ans_list)
    check_list.remove(ans)

    round_check = random.sample(check_list, k=3)
    round_check.append(ans)
    round_check = random.sample(round_check, k=4)
    color_list = random.sample(color_list, k=4)

    print(round_check)
    print(ans)
    return ans

class GameButton(nextcord.ui.View):
    def __init__(self):
        super().__init__()
        self.value = 0
        self.timeout = 2

    @nextcord.ui.button(row=0)
    async def one(self, button: nextcord.ui.Button, interaction: Interaction):
        self.value = 1
        self.stop()

    @nextcord.ui.button(row=0)
    async def two(self, button: nextcord.ui.Button, interaction: Interaction):
        self.value = 2
        self.stop()
    
    @nextcord.ui.button(row=1)
    async def three(self, button: nextcord.ui.Button, interaction: Interaction):
        self.value = 3
        self.stop()
    
    @nextcord.ui.button(row=1)
    async def four(self, button: nextcord.ui.Button, interaction: Interaction):
        self.value = 4
        self.stop()


class Game(commands.Cog):
    
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def gameb(self, ctx):
        ans = round_ans()
        ans_index = round_check.index(ans)
        target_index = color_list.index(dict[ans])
        view = GameButton()

        view.one.label = round_check[0]
        view.two.label = round_check[1]
        view.three.label = round_check[2]
        view.four.label = round_check[3]
        view.one.style = color_list[0]
        view.two.style = color_list[1]
        view.three.style = color_list[2]
        view.four.style = color_list[3]

        global x
        x = bool(random.getrandbits(1))
        if x == True:
            await ctx.send("準備：我要" + ans + "字", delete_after=0.5)
        else:
            await ctx.send("準備：我要" + ans, delete_after=0.5)

        PlayButton = await ctx.send("GO!", view=view)
        await view.wait()
        """await PlayButton.delete()"""
        view.disabled = True

        y = False
        if x == True:
            if view.value == ans_index+1:
                y = True
        else:
            if view.value == target_index+1:
                y = True
        
        if y == True:
            await ctx.send("對，生日快樂")
        else:
            await ctx.send("錯，不過都生日快樂", delete_after=30)
        

def setup(client):
    client.add_cog(Game(client))