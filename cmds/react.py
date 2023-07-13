import discord
from discord.ext import commands
from core.classes import Cog_Extension
import random
import json

with open('setting.json','r',encoding='utf8')as ifile:
    jdate=json.load(ifile)

class React(Cog_Extension):
  
    @commands.command()
    async def web(self,ctx):
        random_pic=random.choice(jdate['url_pic'])
        await ctx.send(random_pic)
        
async def setup(bot):
    await bot.add_cog(React(bot))