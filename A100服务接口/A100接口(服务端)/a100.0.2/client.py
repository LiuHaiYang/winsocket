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
            # new_data = b'[Data: 2015-01-01|000238|AA]'
            # l = len(data_all)
            # print(data_all[2])
            # for x in range(l+1):
            #     if x < l+1:
            #         data = data_all[x]
            #         sock.sendall(bytes(data, encoding='utf-8'))
                # else:
                    # sock.sendall(b'[DataEnd]')
            for  data in data_all:
                sock.sendall(bytes(data,encoding='utf-8'))
                # if data ==b' ':
                #     sock.sendall(b'[DataEnd]')
                data_rec = sock.recv(BUFSIZ)
                print(data_rec)
            if data_rec == b'[DataEmty]':
                sock.sendall(b'DataEnd')
            elif data_rec ==b'[DataFail]':
                error=b'error!!!!!!!!!'
                print(error)
            time.sleep(1)
        sock.close()
if __name__ == '__main__':
    Client()