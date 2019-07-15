import discord
import json
import os
import requests
import time

TOKEN = 'MzA0OTI0NTQxNjIzNDY4MDMz.XSAQSA.kC3eDiJgmkeWW-jgfagKDdSa4wY' #discord bot token
proxythlist = []
client = discord.Client()

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return
    if message.content.startswith('!proxy' or '!Proxy' ):
        async def fate0proxy(message):
            print('[{0}]: {1} want get Fate0 proxy'.format(time.ctime(),message.author.mention))
            url = 'https://raw.githubusercontent.com/fate0/proxylist/master/proxy.list'
            res = requests.get(url)
            if res.status_code == 200:
                for x in res.content.splitlines():
                    json_text = json.loads(x)
                    ipport = "{0}:{1}".format(json_text['host'],json_text['port'])
                    if json_text['country'] == 'TH' or json_text['country'] == 'th':
                        proxythlist.append(ipport)
                print('[{0}]: GET TH PROXY: {1}'.format(time.ctime(),len(proxythlist)))
                with open('proxy_Th.txt', 'w') as file_handler:
                    for x in proxythlist:
                        file_handler.write("{0}\n".format(x))
                return True
            else:
                print('FATE0 HTTP CODE != 200')
                return False
        res = await fate0proxy(message)
        if res == True:
            await message.channel.send('Proxy TH: {0}'.format(len(proxythlist)),file=discord.File('proxy_Th.txt'))
        else:
            await message.channel.send('Fail get Fate0!')
        if os.path.exists("proxy_Th.txt"):
            os.remove("proxy_Th.txt")
            print('[{0}]: DEL proxy_Th.txt'.format(time.ctime()))
        proxythlist.clear()
        print('[{0}]: RESET VAR {1}'.format(time.ctime(),len(proxythlist)))
    if message.content.startswith('!ping'):
        await message.channel.send('pong!')



@client.event
async def on_ready():
    msg = 'Logged in as {0} [{1}]'.format(client.user.name,client.user.id)
    print('{0}'.format('-'*len(msg)))
    print(msg)
    print('{0}'.format('-'*len(msg)))
    await client.change_presence(activity=discord.Game(name='bot by sctnightcore')) 
client.run(TOKEN)


