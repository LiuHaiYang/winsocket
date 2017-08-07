# codinf=utf-8
import socket
import time
HOST='127.0.0.1'
POST=20001
BUFSIZ=1024
def Client():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((HOST, POST))  # 链接服务器
    while 1:
        conn_ok = sock.recv(BUFSIZ)
        print(conn_ok)
        while 1:
            data_all = ['aa3','aa3','aa3','aa3','aa3','aa3','aa3','bb3']#从数据库拿出来的数据
            for  data in data_all:
                sock.sendall(bytes(data,encoding='utf-8'))
                data_rec = sock.recv(BUFSIZ)
                print(data_rec)
            if data_rec ==b'[DataFail]':
                error=b'error!!!!!!!!!'
                print(error)
            c_test = input()
            sock.sendall(bytes(c_test, encoding='utf-8'))
            # sock.sendall(bytes(data,encoding='utf-8'))  # 发送数据给服务器
            time.sleep(1)
            if data_rec == b'[DataEmty]':
                data_end = b'DataEnd'
                sock.sendall(bytes(data_end,encoding='utf-8'))
            # data_rec = sock.recv(BUFSIZ)  # 接收服务器发过来到数据
            print(data_rec)
        # sock.close()
if __name__ == '__main__':
    Client()