from socket import *

# socketserver的请求处理器默认行为是接受连接，获取请求，然后关闭连接
#这使得我们需要像UDP一样，每次向服务器发送消息时都创建一个新的套接字
#服务器的处理程序将套接字通信像文件一样对待，因此需要手动加入终止符（\r\n）


#设置基本参数
HOST = "127.0.0.1"
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST,PORT)


while True:
    tcpCliSock = socket(AF_INET,SOCK_STREAM)
    tcpCliSock.connect(ADDR)
    data = input("May I help you? ")
    if not data:
        break
    tcpCliSock.send(b"%s\r\n"%(bytes(data,"utf-8")))
    data = tcpCliSock.recv(BUFSIZ)
    if not data:
        break
    print(data.strip().decode("utf-8"))
    tcpCliSock.close()
