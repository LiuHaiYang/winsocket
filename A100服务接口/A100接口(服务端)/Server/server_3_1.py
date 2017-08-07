from socket import *
from time import ctime
import os

print(os.getpid())
HOST='127.0.0.1'
POST=20001
BUFSIZ=1024
ADDR=(HOST,POST)#这里是配置套接字，比C语言的简单多了，没那么多结构体

tcpServerSocket=socket(AF_INET,SOCK_STREAM)#建立服务端的套接字
tcpServerSocket.bind(ADDR)#将地址与套接字绑定
tcpServerSocket.listen(5)#然后就是监听
try:
    while True:
        tcpClientSocket,clientaddr=tcpServerSocket.accept()#返回结果
        print(b'...connected from :',clientaddr)
        while True:
            data=tcpClientSocket.recv(BUFSIZ)
            if not data:
                break
            tcpClientSocket.sendall(bytes(data,encoding='utf-8'))
            print(data)
        else:
            tcpClientSocket.close()
except Exception as e:
    print(e)
finally:
    tcpServerSocket.close()