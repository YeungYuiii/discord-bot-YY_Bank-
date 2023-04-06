import nextcord
from nextcord import Interaction
from nextcord.ext import commands
import sqlite3 as sl


class Admin(commands.Cog):

    def __init__(self,client):
        self.client = client

    
def setup(client):
    client.add_cog(Admin(client))