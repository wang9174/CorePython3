from socketserver import (TCPServer as TCP,
                          StreamRequestHandler as SRH)
from  time import ctime

HOST = ""
PORT = 21567
ADDR = (HOST,PORT)

class MyRequeatHandler(SRH):  #继承与实例化请求处理器类 
    def handle(self):  #重写handle方法
        print("...Connecting from: ",self.client_address)
        temp = self.rfile.readline()
        print(type(temp))
        self.wfile.write(b"[%s]%s"%(bytes(ctime(),"utf-8"),temp))

tcpServ = TCP(ADDR,MyRequeatHandler)  #设置地址与事件处理器
print("waiting for connection...")
tcpServ.serve_forever()  #开启服务器无限循环

