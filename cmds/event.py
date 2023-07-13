import discord
from discord.ext import commands
from core.classes import Cog_Extension
from discord import Emoji
import json
import asyncio
import random
import os
import re
import time
from discord.utils import get
import asyncio

with open('setting.json','r',encoding='utf8')as ifile:
    jdate=json.load(ifile)

class event(Cog_Extension):
  
    @commands.Cog.listener()
    async def on_member_join(self, member : discord.Member, *, reason=None):
        channel=self.bot.get_channel(int(jdate['channel_join']))
        await channel.send(f'{member.mention} 加入了')

    @commands.Cog.listener()
    async def on_member_remove(self, member : discord.Member, *, reason=None):
        channel=self.bot.get_channel(int(jdate['channel_leave']))
        await channel.send(f'{member.mention} 離開了')

    @commands.Cog.listener()
    async def on_message(self, msg):
        key = ['這到底是什麼閃現','這到底什麼閃現']
        keyaaa = ['本本']
        asdfghj = ['你在大聲什麼啦']
        num_format = re.compile(r'^[1-9][0-9]*$')
      
        with open('setting.json','r',encoding='utf8') as jfile:
            jdata = json.load(jfile)
        if msg.channel.id == int(jdata['nsfwchannel']) or msg.channel.id == int(jdata['nsfwchannel2']) or msg.channel.id == int(jdata['test']):
          if len(msg.content) == 6 and msg.author !=self.bot.user:
            it_is = re.match(num_format,msg.content)
            if it_is:
              await msg.channel.purge(limit=1)
              await msg.channel.send("https://nhentai.net/g/"+msg.content)
      
        if msg.content in key and msg.author !=self.bot.user:            
            await msg.channel.send('⠄⠄⠄⠄⠄⠄⠄⠈⠉⠁⠈⠉⠉⠙⠿⣿⣿⣿⣿⣿')
            await msg.channel.send('⠄⠄⠄⠄⠄⠄⠄⠄⣀⣀⣀⠄⠄⠄⠄⠄⠹⣿⣿⣿')
            await msg.channel.send('⠄⠄⠄⠄⠄⢐⣲⣿⣿⣯⠭⠉⠙⠲⣄⡀⠄⠈⢿⣿')
            await msg.channel.send('⠐⠄⠄⠰⠒⠚⢩⣉⠼⡟⠙⠛⠿⡟⣤⡳⡀⠄⠄⢻')
            await msg.channel.send('⠄⠄⢀⣀⣀⣢⣶⣿⣦⣭⣤⣭⣵⣶⣿⣿⣏⠄⠄⣿')
            await msg.channel.send('⠄⣼⣿⣿⣿⡉⣿⣀⣽⣸⣿⣿⣿⣿⣿⣿⣿⡆⣀⣿')
            await msg.channel.send('⢠⣿⣿⣿⠿⠟⠛⠻⢿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣼')
            await msg.channel.send('⠄⣿⣿⣿⡆⠄⠄⠄⠄⠳⡈⣿⣿⣿⣿⣿⣿⣿⣿⣿')
            await msg.channel.send('⠄⢹⣿⣿⡇⠄⠄⠄⠄⢀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿')
            await msg.channel.send('⠄⠄⢿⣿⣷⣨⣽⣭⢁⣡⣿⣿⠟⣩⣿⣿⣿⠿⠿⠟')
            await msg.channel.send('⠄⠄⠈⡍⠻⣿⣿⣿⣿⠟⠋⢁⣼⠿⠋⠉⠄⠄⠄⠄')
            await msg.channel.send('⠄⠄⠄⠈⠴⢬⣙⣛⡥⠴⠂⠄⠄⠄⠄⠄⠄⠄⠄⠄')

        if msg.content in asdfghj and msg.author !=self.bot.user:            
            await msg.channel.send('<:__:550972988426682389>')    
          
        with open('setting.json','r',encoding='utf8') as jfile:
            jdata = json.load(jfile)
        if msg.channel.id == int(jdata['nsfwchannel']):
          if msg.content in keyaaa and msg.author !=self.bot.user:
            await msg.channel.send("請稍後..")
            await msg.channel.purge(limit=1)
            await msg.channel.send("亂數生成中...")
            await asyncio.sleep(2)
            await msg.channel.purge(limit=1)
            A=str(random.randint(10,43))
            B=str(random.randint(0,9))
            C=str(random.randint(0,9))
            D=str(random.randint(0,9))
            E=str(random.randint(0,9))
            await msg.channel.purge(limit=1)
            await msg.channel.send("https://nhentai.net/g/"+A+B+C+D+E)
          
    @commands.Cog.listener()
    async def on_raw_reaction_add(self,data):#新增反應貼圖獲取身分組
        if data.message_id==972026677557329921:#判斷反應訊息是否為指定訊息
          if str(data.emoji)=='<:good:911113245266432031>':#判斷反應貼圖移除相對應身分組
            guild= self.bot.get_guild(data.guild_id)  #取得當前所在伺服器
            role = guild.get_role(642003792858054679) #取得伺服器內指定的身分組
            await data.member.add_roles(role)#給予指定的身分組
            #await data.member.send(f'你取得了{role}身分組!')
        if data.message_id==972249059828068362:
          if str(data.emoji)=='<:qqqqq:671001942092414981>':
            guild= self.bot.get_guild(data.guild_id)
            role = guild.get_role(586064514978545664)
            await data.member.add_roles(role)
          if str(data.emoji)=='<:chiwawa2:778626611594919976>':
            guild= self.bot.get_guild(data.guild_id)
            role = guild.get_role(586063944330772520)
            await data.member.add_roles(role)
          if str(data.emoji)=='<:BibleThump:552474452110213120>':
            guild= self.bot.get_guild(data.guild_id)
            role = guild.get_role(586064385152385029)
            await data.member.add_roles(role)
          if str(data.emoji)=='<:winnie:634062164478656543>':
            guild= self.bot.get_guild(data.guild_id)
            role = guild.get_role(586064474436534286)
            await data.member.add_roles(role)
          if str(data.emoji)=='<:deway:629697678934278157>':
            guild= self.bot.get_guild(data.guild_id)
            role = guild.get_role(586064583635107865)
            await data.member.add_roles(role)
          if str(data.emoji)=='<:chiwawa:770313673109012523>':
            guild= self.bot.get_guild(data.guild_id)
            role = guild.get_role(586064693152579584)
            await data.member.add_roles(role)
          if str(data.emoji)=='<:BambooRat3:628571602627330048>':
            guild= self.bot.get_guild(data.guild_id)
            role = guild.get_role(586067885743669269)
            await data.member.add_roles(role)
          if str(data.emoji)=='<:BambooRat2:628571582045880366>':
            guild= self.bot.get_guild(data.guild_id)
            role = guild.get_role(599601855814828062)
            await data.member.add_roles(role)

        if data.message_id==972254682099613756:
          if str(data.emoji)=='<:BloodTrail:550799531906695168>':
            guild= self.bot.get_guild(data.guild_id)
            role = guild.get_role(620188989277863947)
            role2=guild.get_role(972265052293971998)
            await data.member.add_roles(role)
            await data.member.add_roles(role2)
      


  
    @commands.Cog.listener()
    async def on_raw_reaction_remove(self,data):#移除反應貼圖獲取身分組
        if data.message_id==972026677557329921:#判斷反應訊息是否為指定訊息
          if str(data.emoji)=='<:good:911113245266432031>':#判斷反應貼圖移除相對應身分組
            guild = self.bot.get_guild(data.guild_id)#取得當前所在伺服器
            user=guild.get_member(data.user_id)#取得使用者
            role=guild.get_role(642003792858054679)#取得伺服器內指定的身分組
            await user.remove_roles(role)#移除指定的身分組
            #await user.send(f'你移除了{role}身分組!')
        if data.message_id==972249059828068362:
          if str(data.emoji)=='<:qqqqq:671001942092414981>':
            guild= self.bot.get_guild(data.guild_id)
            user=guild.get_member(data.user_id)
            role = guild.get_role(586064514978545664)
            await user.remove_roles(role)
          if str(data.emoji)=='<:chiwawa2:778626611594919976>':
            guild= self.bot.get_guild(data.guild_id)
            user=guild.get_member(data.user_id)
            role = guild.get_role(586063944330772520)
            await user.remove_roles(role)
          if str(data.emoji)=='<:BibleThump:552474452110213120>':
            guild= self.bot.get_guild(data.guild_id)
            user=guild.get_member(data.user_id)
            role = guild.get_role(586064385152385029)
            await user.remove_roles(role)
          if str(data.emoji)=='<:winnie:634062164478656543>':
            guild= self.bot.get_guild(data.guild_id)
            user=guild.get_member(data.user_id)
            role = guild.get_role(586064474436534286)
            await user.remove_roles(role)
          if str(data.emoji)=='<:deway:629697678934278157>':
            guild= self.bot.get_guild(data.guild_id)
            user=guild.get_member(data.user_id)
            role = guild.get_role(586064583635107865)
            await user.remove_roles(role)
          if str(data.emoji)=='<:chiwawa:770313673109012523>':
            guild= self.bot.get_guild(data.guild_id)
            user=guild.get_member(data.user_id)
            role = guild.get_role(586064693152579584)
            await user.remove_roles(role)
          if str(data.emoji)=='<:BambooRat3:628571602627330048>':
            guild= self.bot.get_guild(data.guild_id)
            user=guild.get_member(data.user_id)
            role = guild.get_role(586067885743669269)
            await user.remove_roles(role)
          if str(data.emoji)=='<:BambooRat2:628571582045880366>':
            guild= self.bot.get_guild(data.guild_id)
            user=guild.get_member(data.user_id)
            role = guild.get_role(599601855814828062)
            await user.remove_roles(role)
            
        if data.message_id==972254682099613756:
          if str(data.emoji)=='<:BloodTrail:550799531906695168>':
            guild= self.bot.get_guild(data.guild_id)
            user=guild.get_member(data.user_id)
            role = guild.get_role(620188989277863947)
            role2=guild.get_role(972265052293971998)
            await user.remove_roles(role)
            await user.remove_roles(role2)
    

async def setup(bot):  
    await bot.add_cog(event(bot))  