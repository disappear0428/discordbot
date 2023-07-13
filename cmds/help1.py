import discord
from discord.ext import commands
import json
import random
import os
import time
import datetime
from discord.utils import get
import asyncio
from os.path import dirname
from os.path import join, dirname
from dotenv import load_dotenv
from asyncio import sleep
#from pretty_help import DefaultMenu, PrettyHelp
from core.classes import Cog_Extension
from discord import Emoji


with open('setting.json','r',encoding='utf8')as ifile:
    jdate=json.load(ifile)

class help(Cog_Extension):

    @commands.command()
    async def help(self, ctx):
        embed = discord.Embed(title="機器人幫助面板", description="指令有些有限定使用者或頻道")
        embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar.url)
        embed.add_field(name="[hel", value="顯示抽卡指令", inline=True)        
        embed.add_field(name="[時間", value="顯示現在時間", inline=True)
        embed.add_field(name="[em", value="顯示機器人製作者", inline=True)
        embed.add_field(name="[ping", value="顯示機器人延遲", inline=True)
        embed.add_field(name="[clear 數字", value="清除文字", inline=True)
        embed.add_field(name="[公告 內容", value="幫你公告訊息", inline=True)
        embed.add_field(name="[重複 內容", value="重複你的一段話", inline=True)
        embed.add_field(name="[choose 1,2,3", value="幫你做選擇", inline=True)
        embed.add_field(name="[giveaaaaa", value="加入aaaaa身分組", inline=True)
        embed.add_field(name="[removeaaaaa", value="離開aaaaa身分組", inline=True)
        embed.add_field(name="[move @成員", value="幫你把它移動到失智兒童中心", inline=True)
        embed.add_field(name="[nhentai 數字", value="幫你亂數生成本本|限定頻道", inline=True)
        embed.add_field(name="[你在大聲什麼啦", value="顯示你在大聲什麼啦貼圖", inline=True)
        embed.add_field(name="[加入", value="讓機器人加入你所在的頻道", inline=True)
        embed.add_field(name="[離開", value="讓機器人離開你所在的頻道", inline=True)
        embed.add_field(name="[進進出出", value="讓機器人進出頻道", inline=True)
        embed.add_field(name="[投票 問題 選項1 選項2", value="可以讓大家投票 最多10個選項", inline=True)
        embed.add_field(name="[set_time 數字", value="設置幾幾分的時候發本本(0000~2359)", inline=True)
        embed.add_field(name="[set_channe 頻道ID", value="設置在哪個頻道通知機器人還活著", inline=True)
        embed.add_field(name="[set_nsfwchannel 頻道ID", value="設置本本頻道", inline=True)
        embed.add_field(name="[set_tell_the_time 數字", value="設置幾分的時候報時(00~60)", inline=True)
        embed.add_field(name="[load", value="加載該機器人py檔", inline=True)
        embed.add_field(name="[reload", value="重新載入機器人py檔", inline=True)
        embed.add_field(name="[unload", value="不要加載該機器人py檔", inline=True)
        embed.set_footer(text=f'製作者 By Disappear0428#8509') 
        await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(help(bot))