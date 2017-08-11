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
    # 这里我们就像在“3. 实现最简单的与图灵机器人的交互”中做的一样
    # 构造了要发送给服务器的数据
    apiUrl = 'http://sandbox.api.simsimi.com/request.p?key='+KEY+'&lc=ch&ft=1.0&text='+msg
    try:
        r = requests.get(apiUrl).json()
        # 字典的get方法在字典没有'text'值的时候会返回None而不会抛出异常
        return r.get('response')
    # 为了防止服务器没有正常响应导致程序异常退出，这里用try-except捕获了异常
    # 如果服务器没能正常交互（返回非json或无法连接），那么就会进入下面的return
    except:
        # 将会返回一个None
        return
# 这里是我们在“1. 实现微信消息的获取”中已经用到过的同样的注册方法
@itchat.msg_register(itchat.content.TEXT)
def tuling_reply(msg):
    # 默认回复
    defaultReply = '其实我是个机器人。。我的大脑正在宕机。'
    # 如果小黄鸡出现问题，那么reply将会是None
    reply = get_response(msg['Text'])
    time.sleep(random.randint(0,30))
    # a or b的意思是，如果a有内容，那么返回a，否则返回b
    # 有内容一般就是指非空或者非None，你可以用`if a: print('True')`来测试
    return reply or defaultReply
itchat.auto_login(enableCmdQR=-2, hotReload=True)
itchat.run()