import nextcord
from nextcord import Interaction

class Callings(nextcord.ui.View):
    def __init__(self):
        super().__init__()
        self.value = 0
        self.timeout = 30

    @nextcord.ui.button(label = "檢查結餘/欠餘", style=nextcord.ButtonStyle.blurple)
    async def check(self, button: nextcord.ui.Button, interaction: Interaction):
        self.value = 1
        self.stop()

    @nextcord.ui.button(label = "入數", style=nextcord.ButtonStyle.green)
    async def trans_in(self, button: nextcord.ui.Button, interaction: Interaction):
        self.value = 2
        self.stop()
    
    @nextcord.ui.button(label = "借錢", style=nextcord.ButtonStyle.green)
    async def trans_out(self, button: nextcord.ui.Button, interaction: Interaction):
        self.value = 3
        self.stop()
    
    @nextcord.ui.button(label = "取消", style=nextcord.ButtonStyle.red, row=1)
    async def cencel(self, button: nextcord.ui.Button, interaction: Interaction):
        self.value = 4
        self.stop()

class Cencels(nextcord.ui.View):
    def __init__(self):
        super().__init__()
        self.value = 0

    @nextcord.ui.button(label = "取消", style=nextcord.ButtonStyle.red)
    async def cencel(self, button: nextcord.ui.Button, interaction: Interaction):
        self.value = 1
        self.stop()


