# codinf=utf-8
import socket
import time
def Client():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(('127.0.0.1', 8000))  # 链接服务器
    while 1:
        print('Connect Server Ok！')
        while 1:
            ent = input('client >>> ')
            if ent == 'bye':
                print('connect fail!')
                sock.close()
            sock.sendall(bytes(ent,encoding='utf-8'))  # 发送数据给服务器
            time.sleep(1)
            data = sock.recv(1024)  # 接收服务器发过来到数据
            print(b'server : '+ data)
        sock.close()
if __name__ == '__main__':
    Client()