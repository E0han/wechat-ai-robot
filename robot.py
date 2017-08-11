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
    print("Fri>"+msg['Text'])
    defaultReply = '等下'
    reply = get_response(msg['Text'])
    print("Me>"+reply)
    time.sleep(random.randint(0,20))
    # a or b的意思是，如果a有内容，那么返回a，否则返回b
    return reply or defaultReply
itchat.auto_login(enableCmdQR=-2, hotReload=True)
itchat.run()