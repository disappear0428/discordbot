import discord
from discord.ext import commands
import json
import random
import os
import time
from discord.utils import get
import asyncio
#import keep_alive
from os.path import dirname
#from os.path import join, dirname
from dotenv import load_dotenv
from asyncio import sleep
import datetime
# from discord import guild
# from discord_slash import SlashCommand
# from discord_slash import SlashContext
# from discord_slash.utils.manage_command import create_choice
# from discord_slash.utils.manage_command import create_option


intents = discord.Intents.all()
intents.members = True
# bot = discord.Client()


with open('setting.json','r',encoding='utf8')as ifile:
    jdate=json.load(ifile)

bot = commands.Bot(command_prefix='[',intents=intents)#指令前綴
#discord.Status.<狀態>，可以是online（上線）,offline（下線）,idle（閒置）,dnd（請勿打擾）,invisible（隱身）
機器人狀態 = discord.Status.dnd

#這邊設定機器當前的狀態文字
#type可以是playing（遊玩中）、streaming（直撥中）、listening（聆聽中）、watching（觀看中）、custom（自定義）
#機器人正在遊玩 = discord.Activity(type=discord.ActivityType.watching, name="免費勞工")
bot.remove_command('help')
bot.remove_command('hel')
arr = ['限定1','限定2','3star', '2star', '1star']
rate = [0.5, 0.5, 33, 33, 33]#控制機率
img_限定1='<:A_:783427449396002866>'#discord img
img_限定2='<:deway:629697678934278157>'
img_3star='<:BambooRat3:628571602627330048>'
img_2star='<:BambooRat2:628571582045880366>'
img_1star='<:BambooRat1:628571466438279168>'


@bot.command()
async def 抽卡(ctx,som:str=''):#som為抓 "!抽卡" 後的文字
    card = [None]*10
    for i in range(10):
        prob_card=arr[random_index(rate)]#先給定  避免每次if都是不同的

        if prob_card == '限定1':#去discord加表情後，反斜線\+表情按送出，所顯示的那一串 自行更改
            card[i]=img_限定1
        elif prob_card == '限定2':
            card[i]=img_限定2
        elif prob_card == '3star':
            card[i]=img_3star
        elif prob_card == '2star':
            card[i]=img_2star
        elif prob_card == '1star':
            card[i]=img_1star
        else:
            card[i]=img_1star

    if card.count(img_1star)==10:#保底
        for x in range(9,-1,-1):
            if  card[x]==img_1star:
                card[x]=img_2star
                break

    msg=''
    if card.count(img_1star)==9:#保底嘲諷
        if card.count(img_3star)!=1:
            msg=''

    if card.count(img_3star)>=1:#抽到彩的恭喜
        msg=''

    if card.count(img_限定2)>=1:#抽到限定2的恭喜
        msg=''

    if card.count(img_限定1)>=1:#抽到限定1的恭喜
        msg=''

    lol="".join('%s' %id for id in card)
    await ctx.send('>>'+lol+msg+som+'<<')#ctx.message.author獲取discord用戶id

@bot.command()
async def 抽卡機率(ctx):
    await ctx.send( "限定.."+'{:>5}'.format(str(rate[0]))+"%\n"
                    "限定2.."+'{:>5}'.format(str(rate[1]))+"%\n"
                    "白的  "+'{:>5}'.format(str(rate[2]))+"%\n"
                    "沒問題"+'{:>5}'.format(str(rate[3]))+"%\n"
                    "有問題"+'{:>5}'.format(str(rate[4]))+"%\n")
@bot.command()
async def hel(ctx):
    embed = discord.Embed(title="抽卡機器人", description="以下是指令")
    embed.add_field(name="[抽卡", value="抽10張卡 有保底", inline=False)
    embed.add_field(name="[抽卡 空格 \'任意文字\' ", value="與抽卡相同，後方輸入的任意文字會回傳", inline=False)
    embed.add_field(name="[抽卡機率", value="顯示當前抽卡機率", inline=False)
    await ctx.send(embed=embed)

def random_index(rate):
    start = 0
    index = 0
    randnum = random.randint(1, sum(rate))

    for index, scope in enumerate(rate):
        start += scope
        if randnum <= start:
            break
    return index


@bot.event
async def on_ready():
    pid=os.getpid()
    log = bot.get_channel(604249473589182464)
    await log.send('成功啟動'+'\n'+str(pid))
    for filename in os.listdir('./cmds'):
        if filename.endswith('.py'):
            try:
                await bot.load_extension(f'cmds.{filename[:-3]}')
                print(f'✅   已加載 {filename}')
            except Exception as error:
                print(f'❎   {filename} 發生錯誤  {error}')  
    #await bot.change_presence(status= 機器人狀態, activity=機器人正在遊玩)
    print(">> 機器人上線了 <<")#機器人上線
    伺服器 = len(bot.guilds)
    使用者 = len(bot.users)
    await bot.wait_until_ready()
    狀態列表 = ["免費勞工", f" {伺服器} 個伺服器", "使用[help查看指令",f"監視 {使用者} 名使用者"]
    while True:
      正在遊玩 = discord.Game(random.choice(狀態列表))
      await bot.change_presence(status=機器人狀態, activity=正在遊玩)
      await asyncio.sleep(300)
    

    

@bot.command()
async def load(ctx, extension):
    if ctx.author.id == 407560614378995713 or 377760740473569291:
      await bot.load_extension(f"cmds.{extension}")
      await ctx.send(f'Loaded {extension} done')
    else:
      await ctx.send("你沒有權限使用")

@bot.command()
async def unload(ctx, extension):
    if ctx.author.id == 407560614378995713 or 377760740473569291:
      await bot.unload_extension(f"cmds.{extension}")
      await ctx.send(f'Un - Loaded {extension} done')
    else:
      await ctx.send("你沒有權限使用")

@bot.command()
async def reload(ctx, extension):
    if ctx.author.id == 407560614378995713 or 377760740473569291:
      await bot.reload_extension(f"cmds.{extension}")
      await ctx.send(f'Re - Loaded {extension} done')
    else:
      await ctx.send("你沒有權限使用")   




@bot.command()
async def 加入(ctx):
    #channel = discord.utils.get(ctx.guild.channels,name= "失智兒童中心") #加入到指定頻道
    channel = ctx.message.author.voice.channel  #加入到打指令使用者所在的頻道
    await channel.connect()
  
@bot.command()
async def 離開(ctx):
    await ctx.voice_client.disconnect()

@bot.command()
async def 進進出出(ctx):
    await ctx.channel.purge(limit=1)
    await ctx.send("我進來了")
    channel = ctx.message.author.voice.channel  #加入到打指令使用者所在的頻道
    await channel.connect()
    await ctx.send("我又出去了")
    await ctx.voice_client.disconnect()
    

@bot.command()
async def move(ctx,member:discord.Member=None):
    if ctx.author.voice and ctx.author.voice.channel:#判斷輸入指令的人有沒又在頻道裡
        channel = discord.utils.get(ctx.guild.channels,name= "失智兒童中心")
        #channel = discord.utils.get(ctx.guild.channels,name='561144566086893568')
    else:
        await ctx.send("您沒有連接到語音頻道！")
        await ctx.send("立即刪除文字")
        await asyncio.sleep(1)
        await ctx.channel.purge(limit=3)
    if not member:
        await ctx.send("你想要我把誰移出去?     請使用 [move @user")
        await ctx.send("立即刪除文字")
        await asyncio.sleep(1)
        await ctx.channel.purge(limit=3)

    await member.move_to(channel)
    await ctx.send("移動成功")
    await ctx.send("立即刪除文字")
    await asyncio.sleep(1)
    await ctx.channel.purge(limit=3)

@bot.command(pass_context=True)
async def giveaaaaa(ctx):
    roleVer = "aaaaa" #要添加的角色
    user = ctx.message.author #用戶
    role = roleVer # 將名稱從roleVer更改為role
    await ctx.send("""正在加入aaaaa身分組 {}""".format(user))
    try:
        await user.add_roles(discord.utils.get(user.guild.roles, name=role)) #添加身分組
    except Exception as e:
        await ctx.send("運行此命令時發生錯誤 " + str(e)) #如果有錯誤
        await ctx.send("5秒後自動刪除文字")
        await asyncio.sleep(5)
        await ctx.channel.purge(limit=4)
    else:
        await ctx.send("""加入成功: {}""".format(user)) # 沒有錯誤，表示已驗證
        await ctx.send("5秒後自動刪除文字")
        await asyncio.sleep(5)
        await ctx.channel.purge(limit=4)

@bot.command(pass_context=True)
async def removeaaaaa(ctx):
    roleVer = "aaaaa" #要添加的角色
    user = ctx.message.author #用戶
    role = roleVer # 將名稱從roleVer更改為role
    await ctx.send("""正在離開aaaaa身分組 {}""".format(user))
    try:
        await user.remove_roles(discord.utils.get(user.guild.roles, name=role)) #刪除身分組
    except Exception as e:
        await ctx.send("運行此命令時發生錯誤  "+ str(e)) #如果有錯誤
        await ctx.send("5秒後自動刪除文字")
        await asyncio.sleep(5)
        await ctx.channel.purge(limit=4)
    else:
        await ctx.send("""成功離開: {}""".format(user)) # 沒有錯誤，表示已驗證
        await ctx.send("5秒後自動刪除文字")
        await asyncio.sleep(5)
        await ctx.channel.purge(limit=4)

@bot.command(pass_context=True)
async def time(ctx):
    now_time = datetime.datetime.now()
    hour =datetime.timedelta(hours=8)
    new_time=now_time + hour
    await ctx.channel.send(new_time.strftime('%Y-%m-%d %H:%M:%S'))
    await ctx.send("5秒後自動刪除文字")
    await asyncio.sleep(5)
    await ctx.channel.purge(limit=3)


@bot.event
async def on_member_join(member):
    await sleep(5)
    for channel in member.guild.channels:
        if channel.name.startswith('伺服器總人數'):
            await channel.edit(name=f'伺服器總人數: {member.guild.member_count}')
            break

@bot.event
async def on_member_remove(member):
    await sleep(5)
    for channel in member.guild.channels:
        if channel.name.startswith('伺服器總人數'):
            await channel.edit(name=f'伺服器總人數: {member.guild.member_count}')
            break

@bot.event
async def on_reaction_add(reaction, user):
    channel = discord.utils.get(user.guild.channels, name="大廳")
    print(reaction.message.id)
    if reaction.message.author.id == 525370209176125440:
        # 我建議改用 id，因為任何用戶都可以使用您的機器人名稱
        if user.id != 525370209176125440 and reaction.message.channel == channel:
            cache_msg = discord.utils.get(bot.cached_messages, id=reaction.message.id)
            print(cache_msg.reactions)
            print(reaction.emoji)

            # 檢查 cache_msg 中的每個反應
            for r in cache_msg.reactions:
                # 檢查用戶是否是反應的作者
                # 並檢查用戶是否不是機器人
                # 並檢查這個反應表情符號是否不是他們剛剛做出反應的表情符號
                if user in await r.users().flatten() and not user.bot and str(r) != str(reaction.emoji):
                    # 刪除他們之前的反應
                    await cache_msg.remove_reaction(r.emoji, user)
                    

if __name__ == "__main__":    
    bot.run(jdate['TOKEN'])