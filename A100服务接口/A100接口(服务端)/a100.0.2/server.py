# coding=utf-8
import socket
import re_test
# Server
HOST='127.0.0.1'
POST=20001
BUFSIZ=1024
def Server():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((HOST, POST))
    sock.listen(5)  # 监听，最大链接数
    while 1:
        connection, address = sock.accept()  # 开始接受请求,进入等待阻塞状态，直到有链接到达
        ok = '[ConnectData]'
        connection.sendall(bytes(ok, encoding='utf-8'))
        while 1:
            data_rev = connection.recv(BUFSIZ)  # 接收客户端发过来的数据  #对data_rev进行解析，是否为所需的正确数据
            if  data_rev != '':#数据
                data = data_rev
                print(data)
                error = b'bb3'
                if data != error:#正确的数据
                    data_ok = '[DataOK]'
                    connection.sendall(bytes(data_ok, encoding='utf-8'))
                elif data == error:#不正确数据
                    data_fail = '[DataFail]'
                    connection.sendall(bytes(data_fail, encoding='utf-8'))
                else:
                    pass
            elif data_rev ==b'[DataTest]':#测试
                connection.sendall(b'TestOK')
            elif data_rev ==b'[DataEnd]':#数据发送完毕 或者   已经清空缓存
                data_over = b'dataend!!!!!!!!!!!!!!'
                print(data_over)

        s_emty = input()
        connection.sendall(bytes(s_emty, encoding='utf-8'))
        data_emty = connection.recv(BUFSIZ)  # 接收客户端发过来清空数据缓存的消息
        print(data_emty)

if __name__ == '__main__':
    Server()