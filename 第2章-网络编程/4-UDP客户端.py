from socket import *


#设置基础参数
HOST = "127.0.0.1"
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST,PORT)

#创建套接字
udpCliSock = socket(AF_INET,SOCK_DGRAM)

#进入数据发送循环
while True:
    data = input("Excuse me?")
    if not data:
        break
    udpCliSock.sendto(bytes(data,"utf-8"),ADDR)  # 由于udp不创建连接，所以发送消息需要附带地址（包含ip和端口）
    data,ADDR = udpCliSock.recvfrom(BUFSIZ)
    if not data:
        break
    print(data.decode("utf-8"))  #需要decode之后再输出，否则会出现 b""

udpCliSock.close()

