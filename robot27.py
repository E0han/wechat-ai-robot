#Wechat-auto_reply-robot
#coding="uft-8"
#__date__='2017.8.10'
#__author__=='0han'

from itchat.content import *
import itchat 
import time
import requests
import random

print "====Wechat-AI===Start===="

KEY = '30bef77f-d0ad-4030-9e6c-dae0b3ccef81'

def get_response(msg):
    apiUrl = 'http://sandbox.api.simsimi.com/request.p?key='+KEY+'&lc=ch&ft=0.0&text='+msg
    try:
        r = requests.get(apiUrl).json()
        return r.get('response')
    except:
        return
def main():
    @itchat.msg_register(itchat.content.TEXT)
    def tuling_reply(msg):
        defaultReply = 'wait'
        reply = get_response(msg['Text'])
        #time.sleep(random.randint(0,30))
        return reply or defaultReply
    itchat.auto_login(enableCmdQR=-2, hotReload=True)
    itchat.run()

if __name__ == '__main__':
    main()