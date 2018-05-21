#Wechat-auto_reply-robot
#coding="uft-8"
#__date__='2017.8.10'
#__author__=='0han'

from itchat.content import *
import itchat
import time
import requests
import random

print("====Wechat-AI===Start====")

KEY = '30bef77f-d0ad-4030-9e6c-dae0b3ccef81'

def get_response(msg):
    apiUrl = 'http://sandbox.api.simsimi.com/request.p?key='+KEY+'&lc=ch&ft=1.0&text='+msg
    try:
        r = requests.get(apiUrl).json()
        return r.get('response')
    except:
        return
@itchat.msg_register(itchat.content.TEXT)
def tuling_reply(msg):
    defaultReply = 'Wait a moment, the robot is down now'
    reply = "[自动回复] 学习中，请以'1+[你的留言内容]'的格式回复"
    get_reply= "[已收到] 等会回复你"
    time.sleep(random.randint(0,10))
    # a or b的意思是，如果a有内容，那么返回a，否则返回b
    if msg['TEXT'][0]=='1':
        return 
    else:
        return reply or defaultReply
itchat.auto_login(enableCmdQR=-2, hotReload=True)
itchat.run()