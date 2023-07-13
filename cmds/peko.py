import discord
from discord.ext import commands
from discord.ext.commands import Bot
from discord.ext.commands import has_permissions
from core.classes import Cog_Extension
import json
import datetime
import asyncio
import random
import os
import time
from discord.utils import get
from datetime import timedelta
import re


with open('setting.json','r',encoding='utf8')as ifile:
    jdate=json.load(ifile)
    

class peko(Cog_Extension):

    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f'{round(self.bot.latency*1000)} (ms)')

    @commands.command()
    async def em(self, ctx):
        embed=discord.Embed(title="Disappear0428", url="https://replit.com/@stu97305/botnew",
        description="廢物大學生",color=0x3e8cb3, timestamp=datetime.datetime.now())
        embed.set_author(name="關於機器人製作者", icon_url="https://i.imgur.com/3xIb3oY.jpg")
        embed.set_thumbnail(url="https://i.imgur.com/3xIb3oY.jpg")
        await ctx.send(embed=embed)

    @commands.command()
    async def 重複(self, ctx, *,msg):
        if ctx.author.id == 407560614378995713 or 377760740473569291:
          await ctx.message.delete()
          await ctx.send(msg)
        else:
          await ctx.send("你沒有權限使用")
    
    @commands.command()
    async def clear(self, ctx, num:int):
        await ctx.channel.send('正在刪除中...')
        await asyncio.sleep(3)
        await ctx.channel.purge(limit=num+2)
    
    @commands.command()
    async def 你在大聲什麼啦(self, ctx, msg):
        await msg.channel.send('<:__:550972988426682389>')

    @commands.command()
    async def 公告(self,ctx,*,message=None):
        if ctx.author.id == 407560614378995713 or 377760740473569291:
          await ctx.channel.purge(limit=1)
          if message==None:
            await ctx.channel.send("沒有輸入要公告的訊息，請重新輸入")
            await ctx.channel.send("五秒後自動刪除訊息")
            await asyncio.sleep(5)
            await ctx.channel.purge(limit=2)
          else:
            embed = discord.Embed(title='[公告]',description=message)
            embed.set_footer(text=f'公告 By {ctx.author}')  
            await ctx.send(embed=embed)
        else:
          await ctx.send("你沒有權限使用")

    @commands.command()
    async def choose(self, msg,qq):
      #if msg.author.id != 197910562292629504:
         qwe = qq
         q2 = ["就是","窩幫你選擇"]      
         xlist=qwe.split(",")
         await msg.channel.send("窩想想看")
         await asyncio.sleep(2)
         await msg.channel.purge(limit=1)
         await msg.channel.send(random.choice(q2)+"  "+random.choice(xlist)+" 了")   
      
    @commands.command()
    async def nhentai(self, ctx,number):
      with open('setting.json','r',encoding='utf8') as jfile:
          jdata = json.load(jfile)
      if ctx.channel.id == int(jdata['nsfwchannel']):
        await ctx.channel.purge(limit=1)
        for i in range(0,int(number)):
            A=str(random.randint(10,39))
            B=str(random.randint(0,9))
            C=str(random.randint(0,9))
            D=str(random.randint(0,9))
            E=str(random.randint(0,9))
            await ctx.channel.send("https://nhentai.net/g/"+A+B+C+D+E)
      else:
        await ctx.channel.send("該頻道無法使用")
    @commands.command()
    async def set_nsfwchannel(self,ctx,nsfwchannel):
      if ctx.author.id == 407560614378995713 or 377760740473569291:
        with open('setting.json','r',encoding='utf8') as jfile:  #載入setting.json檔案裡面的東西
          jdata = json.load(jfile)
        jdata['nsfwchannel'] = nsfwchannel                       #把time寫入setting裡面的time
        with open('setting.json','w',encoding='utf8') as jfile:
          json.dump(jdata,jfile,indent=4)
      else:
        await ctx.send("你沒有權限使用")

    @commands.command()
    async def 時間(self,ctx):
      await ctx.channel.purge(limit=1)
      now_time = datetime.datetime.now()
      hour =datetime.timedelta(hours=8)
      new_time=now_time + hour
      await ctx.channel.send(new_time.strftime('%Y-%m-%d %H:%M:%S'))

    @commands.command()
    async def 投票(self,ctx,*,cho):
      await ctx.channel.purge(limit=1)
      list = re.compile(r'\S+').findall(cho)
      emoji_num = ['1️⃣','2️⃣','3️⃣','4️⃣','5️⃣','6️⃣','7️⃣','8️⃣','9️⃣','🔟']
      if len(list) > 2:
        embed=discord.Embed(title=list[0],color=0x0011ff)
        list.pop(0)
        count = 0
        for ele in list:
          embed.add_field(name = f"{emoji_num[count]} {ele}",value = "\u200b",inline = False)
          count = count+1
        embed.set_footer(text=f'投票 By {ctx.author}')
        msg = await ctx.send(embed=embed)
        count = 0
        for ele in list:
          await msg.add_reaction(emoji_num[count])
          count = count+1
      else :
        await ctx.channel.send("指令格式輸入錯誤")
        await ctx.channel.send("請輸入[投票 問題 選項1 選項2 選項3....")

async def setup(bot):
    await bot.add_cog(peko(bot))