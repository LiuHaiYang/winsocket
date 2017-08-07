# coding=utf-8
import socket
import re
# Server
HOST='127.0.0.1'
POST=20001
BUFSIZ=1024
def Server():
    #超时设置
    timeout = 20
    socket.setdefaulttimeout(timeout)

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((HOST, POST))
    sock.listen(5)  # 监听，最大链接数
    re1 = '(\\[)'  # Any Single Character 1
    re2 = '((?:[a-z][a-z]+))'  # Word 1
    re3 = '(:)'  # Any Single Character 2
    re4 = '((?:2|1)\\d{3}(?:-|\\/)(?:(?:0[1-9])|(?:1[0-2]))(?:-|\\/)(?:(?:0[1-9])|(?:[1-2][0-9])|(?:3[0-1]))(?:T|\\s)(?:(?:[0-1][0-9])|(?:2[0-3])):(?:[0-5][0-9]):(?:[0-5][0-9]))'  # Time Stamp 1
    re5 = '(\\|)'  # Any Single Character 3
    re6 = '([a-z])'  # Any Single Word Character (Not Whitespace) 1
    re7 = '([\u4e00-\u9fa5])'
    re8 = '(\\])'  # Any Single Character 4
    re9 = '([0-9]{6})'
    rg = re.compile(re1 + re2 + re3 + re4 + re5 + re9 + re5 + re6 + re5 + re7 + re8, re.IGNORECASE | re.DOTALL)
    while 1:
        connection, address = sock.accept()  # 开始接受请求,进入等待阻塞状态，直到有链接到达
        ok = '[ConnectData]'
        connection.sendall(bytes(ok, encoding='utf-8'))
        while 1:
            data_rev = connection.recv(BUFSIZ)  # 接收客户端发过来的数据  #对data_rev进行解析，是否为所需的正确数据
            # print(len(data_rev))
            # print(len(b'[DataFail]'))#  len  = 11
            # print(data_rev)

            #bytes转换 汉字
            data_str = bytes.decode(data_rev)
            # print(data_str)
            if len(data_rev)>11:
                data = data_str
                if re.match(rg,data):#正确的数据
                    data_ok = '[DataOK]'
                    print("Rec:" + data)
                    connection.sendall(bytes(data_ok, encoding='utf-8'))
                else:
                    data_fail = '[DataFail]'
                    connection.sendall(bytes(data_fail, encoding='utf-8'))
            elif data_rev ==b'[DataTest]':#测试
                connection.sendall(b'[TestOK]')
                break
            elif data_rev ==b'[DataEnd]':#数据发送完毕 或者   已经清空缓存
                data_over = b'dataend!!!!!!!!!!!!!!'
                print(data_over)
                break

         #清空缓存
        s_emty = input()
        connection.sendall(bytes(s_emty, encoding='utf-8'))
        # 接收客户端发过来清空数据缓存的消息
        data_end = connection.recv(BUFSIZ)
        print(data_end)
		
##设置超时
#timeout= 60
#socket.setdefaulttimeout(timeout)

if __name__ == '__main__':
    Server()