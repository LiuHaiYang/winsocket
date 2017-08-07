from socket import *

HOST='127.0.0.1'
POST=20001
BUFSIZE=1024
ADDR=(HOST,POST)
tcpClientSocket=socket(AF_INET,SOCK_STREAM)
tcpClientSocket.connect(ADDR)

while True:
    data=input('>')
    if data.lower()=='q':
        break
    tcpClientSocket.sendall(bytes(data,encoding='utf-8'))
    data=tcpClientSocket.recv(BUFSIZE)
    if not data:
        break
    print(data)
tcpClientSocket.close()