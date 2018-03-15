from socket import *
from time import ctime

# UDP服务器不是面对连接的，所以无需像TCP服务器一样创建独立连接，也不用监听传入的连接

#设置基本参数
HOST = ""
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST,PORT)

#创建套接字
udpSerSock = socket(AF_INET,SOCK_DGRAM)
udpSerSock.bind(ADDR)

#开启服务器循环
while 1:
    print("Waiting for message...")
    data,addr = udpSerSock.recvfrom(BUFSIZ)  # recv仅用于接受TCP消息，recvfrom仅用于接受UDP消息
    udpSerSock.sendto(b"[%s] %s"%(bytes(ctime(),"utf-8"),data),addr)  # send用于发送TCP消息，sendto用于发送UDP消息
    print("...received from and returned to:",addr)

udpSerSock.close()  #同样,这一条并不会执行
