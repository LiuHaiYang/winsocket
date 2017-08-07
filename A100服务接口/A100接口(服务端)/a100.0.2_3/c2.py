# codinf=utf-8

import socket
import time
HOST='127.0.0.1'
POST=20001
BUFSIZ=1024
# 超时设置
timeout = 40
socket.setdefaulttimeout(timeout)
def Client():

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((HOST, POST))  # 链接服务器
    while 1:
        conn_ok = sock.recv(BUFSIZ)
        print(conn_ok)
        while 1:
            data_all = ['[Data:2015-01-01 12:00:01|000000|B|放到一]','[Data:2015-01-01 12:00:01|000000|B|的一]',
                        '[Data:2015-01-01 12:00:01|000000|B|大四的就]','[Data:2015-01-01 12:01:01|000000|B|撒一]',
                        '[Data:2016-11-01 12:00:01|000000|B|爱的一]','[Data:2015-01-01 12:00:01|000000|B|地方一]',
                        '[Data:2015-01-01 12:00:01|000000|B|撒一]','[Data:2015-01-01 12:00:01|000000|B|维吾尔一]',
                        '[Data:2015-01-01 12:00:01|000000|B|撒一]','[DataEnd]',
                        'Data:2015-01-01 12:00:01|000000|K|阿斯顿啊个]']
            for data in data_all:
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
            if data_rec == b'[DataEmpty]':
                data_end = 'DataEnd'
                sock.sendall(bytes(data_end,encoding='utf-8'))
            # data_rec = sock.recv(BUFSIZ)  # 接收服务器发过来到数据
            print(data_rec)
        # sock.close()
if __name__ == '__main__':
    Client()