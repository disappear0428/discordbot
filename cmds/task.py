import discord
import json,asyncio,datetime
from discord.ext import commands
from core.classes import Cog_Extension
import random


class Task(Cog_Extension):
  def __init__(self,*args,**kwargs):
    super().__init__(*args,**kwargs)

    self.counter = 0
    self.coun=1

    
    # async def interval():
      # await self.bot.wait_until_ready()#等機器人準備就緒
      # self.channel=self.bot.get_channel(972624852492116070)#獲取頻道
      # while not self.bot.is_closed():  #當機器人沒有關閉的話會一直執行
        # await asyncio.sleep(5)#單位:秒
        # await self.channel.send('我正在運行中')
    # self.bg_task=self.bot.loop.create_task(interval())

    async def time_task():
      await self.bot.wait_until_ready()#等機器人準備就緒
      self.channel1=self.bot.get_channel(972265002797006910)#獲取頻道
      while not self.bot.is_closed():  #當機器人沒有關閉的話會一直執行
        now_time = datetime.datetime.now().strftime('%H%M')
        with open('setting.json','r',encoding='utf8') as jfile:
          jdata = json.load(jfile)
        if now_time == jdata['time'] and self.counter == 0:
          
          self.counter=1
          await self.channel1.send('每日亂數生成10本...')
          for i in range(0,10):
            A=str(random.randint(10,43))
            B=str(random.randint(0,9))
            C=str(random.randint(0,9))
            D=str(random.randint(0,9))
            E=str(random.randint(0,9))
            await self.channel1.send("https://nhentai.net/g/"+A+B+C+D+E)
          await asyncio.sleep(1)
          
        else:
          await asyncio.sleep(1)
          pass
        
    self.bg_task=self.bot.loop.create_task(time_task())

    async def reload_time():
      await self.bot.wait_until_ready()#等機器人準備就緒
      while not self.bot.is_closed():  #當機器人沒有關閉的話會一直執行
        now_time = datetime.datetime.now().strftime('%H%M')
        with open('setting.json','r',encoding='utf8') as jfile:
          jdata = json.load(jfile)
        if now_time == jdata['nextday'] and self.counter == 1:
          self.counter=0
          await asyncio.sleep(1)
          
        else:
          await asyncio.sleep(1)
          pass
      self.bg_task=self.bot.loop.create_task(reload_time())

    async def tell_the_time():
      await self.bot.wait_until_ready()#等機器人準備就緒
      self.channel=self.bot.get_channel(972624852492116070)#獲取頻道      
      while not self.bot.is_closed():  #當機器人沒有關閉的話會一直執行
        now_time = datetime.datetime.now()
        hour =datetime.timedelta(hours=8)
        new_time=now_time + hour
        with open('setting.json','r',encoding='utf8') as jfile:
          jdata = json.load(jfile)
        if new_time.strftime('%M')==jdata['min'] and self.coun == 0 :         
          await self.channel.send(new_time.strftime('%Y-%m-%d %H:%M:%S'))
          self.coun=1
          await asyncio.sleep(1)
        else :
          await asyncio.sleep(1)
          pass
        if new_time.strftime('%M')!=jdata['min'] and self.coun == 1 :
          self.coun = 0
          print(self.coun)
          await asyncio.sleep(1)
        else:
          await asyncio.sleep(1)
          pass           
        
    self.bg_task=self.bot.loop.create_task(tell_the_time())

    
  
    
    

  @commands.command()
  async def set_channel(self,ctx,ch:int):
    if ctx.author.id == 407560614378995713 or 377760740473569291:
      self.channel=self.bot.get_channel(ch)
      await ctx.send(f'已經把頻道設置為{self.channel.mention}')
    else:
      await ctx.send("你沒有權限使用")

  @commands.command()
  async def set_time(self,ctx,time):
    if ctx.author.id == 407560614378995713 or 377760740473569291:
      self.counter=0
      with open('setting.json','r',encoding='utf8') as jfile:  #載入setting.json檔案裡面的東西
        jdata = json.load(jfile)

      jdata['time'] = time                                     #把time寫入setting裡面的time
      with open('setting.json','w',encoding='utf8') as jfile:
        json.dump(jdata,jfile,indent=4)                        #寫入後縮排4字元
    else:
      await ctx.send("你沒有權限使用")

  @commands.command()
  async def set_tell_the_time(self,ctx,min:int):    
    if ctx.author.id == 407560614378995713 or 377760740473569291:
      with open('setting.json','r',encoding='utf8') as jfile:      
        jdata =json.load(jfile)      
      jdata['min']=min
      with open('setting.json','w',encoding='utf8') as jfile:      
        json.dump(jdata,jfile,indent=4)
    else:
      await ctx.send("你沒有權限使用")
    


async def setup(bot):
  await bot.add_cog(Task(bot))
