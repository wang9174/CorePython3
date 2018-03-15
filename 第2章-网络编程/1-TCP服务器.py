import socket
from time import ctime

# TCP时间戳服务器，接收数据，并返回带时间戳的数据

#在Python3中，所有数据的传输都要使用bytes类型（bytes类型只支持ascii码）
#所以要么在发送的字符串前面加b
# 要么使用encode("utf-8)转换成bytes类型发送，但需要在接收端用decode()进行转码


#设置基本参数
HOST = ""  #空白表示接受任何可用的地址（可适用于服务器IP变化的情况）
PORT = 21567   #设置服务器通信端口号
BUFSIZ = 1024   #缓存区大小为1024b
ADDR = (HOST,PORT)  #绑定成元组

#创建套接字并开启监听，设置相关参数
tcpSerSock = socket.socket(socket.AF_INET,socket.SOCK_STREAM) #创建套接字并设置连接类型
# AF_UNIX基于文件的套接字，常用于进程间通信
# AF_INET基于网络的套接字，用于网络通信
# SOCK_STREAM面向连接的套接字（通过TCP协议实现）,建立连接所以无需指定发送给谁
# SOCK_DGRAM无连接的套接字（通过UDP协议实现），无连接所以每次发送都需要指定发送对象
tcpSerSock.bind(ADDR)  #将（主机号，端口）绑定到套接字上
tcpSerSock.listen(5)  #设置并启动监听器，设置最大同时处理的请求数

#进入服务器无限循环，处理连接请求
while True:
    print("Waiting for connection...")
    tcpCliSock, addr = tcpSerSock.accept()  #被动等待客户端连接，直到到达并返回新的套接字和IP地址
    print("...connected from:",addr)  #输出客户端的IP地址

    #创建一个独立循环用于监听并接受TCP消息
    while True:
        date = tcpCliSock.recv(BUFSIZ)  #接收数据并将其实例化为本地变量
        if not date:
            break
        tcpCliSock.send(b"[%s] %s"%(bytes(ctime(),"utf-8"),date)) # %s用于被后面的数据替换
    tcpCliSock.close()  #结束这个客户端的连接

tcpSerSock.close()  #这个语句不会执行，但在需要的时候，我们可以设置条件来结束服务器循环
