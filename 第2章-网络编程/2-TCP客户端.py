import re
from socket import *
# from...import 与import的区别
# 前者导入了具体的成员不需要加模块前缀，后者仅导入了模块因此需要（模块.成员）的方式来使用



#设置基础参数
patten = "^(?:(?:(?:1[0-9][0-9])|(?:2[0-4][0-9])|(?:25[0-5])|(?:[1-9][0-9])|(?:[0-9]))\.){3}(?:(?:1[0-9][0-9])|(?:2[0-4][0-9])|(?:25[0-5])|(?:[1-9][0-9])|(?:[0-9]))$"

while True:
    HOST = input("请输入目标IP地址：")
    PORT = input("请输入端口号：")
    if not HOST:
        HOST = "127.0.0.1"
        PORT = 21567
        print("__IP缺失，将采用默认设置__")
        break
    elif  re.match(patten,HOST) is not None:
        print("__已确认目标IP__")
        break
    else:
        print("__输入的IP地址格式不正确,请重新输入__")

    if not PORT:
        HOST = "127.0.0.1"
        PORT = 21567
        print("__端口缺失，将采用默认设置__")
        break
    elif re.match("^\w{1,9}$",PORT) is not None:
        print("__已确认目标端口__")
        break
    else:
        print("__输入的端口格式不正确，请重新输入__")


PORT = 21567
BUFSIZ = 1024
ADDR = (HOST,PORT)

#创建套接字并连接服务器
tcpCliSock = socket(AF_INET,SOCK_STREAM)
tcpCliSock.connect(ADDR)

#发送数据，接收并处理回执
while True:
    data = input("请输入要传递的数据：")
    if not data:  #判断是否有输入，如果没有输入则跳出循环
        break
    tcpCliSock.send(bytes(data,"utf-8"))  #将输入传递给服务器
    data = tcpCliSock.recv(BUFSIZ)  #接收服务器回复
    if not data:
        break
    print(data.decode("utf-8"))

#结束套接字
tcpCliSock.close()
