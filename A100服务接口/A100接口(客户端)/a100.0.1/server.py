# coding=utf-8
import socket,sys
import re
import threading
from multiprocessing import Pool
import random
# Server
HOST='127.0.0.1'
POST=20001
BUFSIZ=1024

#超时设置
# timeout = 40
# socket.setdefaulttimeout(timeout)
try:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error as e:
    print("Error creating socket: %s"  %e)
    sys.exit()
try:
    sock.bind((HOST, POST))
except socket.error as e:
    print( "Bind failed!")
    sys.exit()
print("Socket bind complete")
sock.listen(10)# 监听，最大链接数
print("Socket now listening")

# re1 = '(\\[)'  # Any Single Character 1
# re2 = '((?:[a-z][a-z]+))'  # Word 1
# re3 = '(:)'  # Any Single Character 2
# re4 = '((?:2|1)\\d{3}(?:-|\\/)(?:(?:0[1-9])|(?:1[0-2]))(?:-|\\/)(?:(?:0[1-9])|(?:[1-2][0-9])|(?:3[0-1]))(?:T|\\s)(?:(?:[0-1][0-9])|(?:2[0-3])):(?:[0-5][0-9]):(?:[0-5][0-9]))'  # Time Stamp 1
# re5 = '(\\|)'  # Any Single Character 3
# re6 = '([a-z])'  # Any Single Word Character (Not Whitespace) 1
# re7 = '([\u4e00-\u9fa5]{2,})'
# re8 = '(\\])'  # Any Single Character 4
# re9 = '([0-9]{6})'
# rg = re.compile(re1 + re2 + re3 + re4 + re5 + re9 + re5 + re6 + re5 + re7 + re8, re.IGNORECASE | re.DOTALL)

def Server():
    try:
        connection, address = sock.accept()  # 开始接受请求,进入等待阻塞状态，直到有链接到达
        ok = '[ConnectOK]'
        connection.sendall(bytes(ok, encoding='utf-8'))
    except sock.error as e:
        print('conn fail :' % e)
    while 1:
        data_rev = connection.recv(BUFSIZ)  # 接收客户端发过来的数据  #对data_rev进行解析，是否为所需的正确数据
        print(data_rev)
        #bytes转换 汉字
        data_str = bytes.decode(data_rev)
        if data_str == '[DataFirst]':
            data =['[Data:2015-01-01 12:00:01|000000|B|放到一]','[Data:2015-01-01 12:00:01|000000|B|的一]',
                        '[Data:2015-01-01 12:00:01|000000|B|大四的就]','[Data:2015-01-01 12:01:01|000000|B|撒一]',
                        '[Data:2016-11-01 12:00:01|000000|B|爱的一]','[Data:2015-01-01 12:00:01|000000|B|地方一]',
                        '[Data:2015-01-01 12:00:01|000000|B|撒一]','[Data:2015-01-01 12:00:01|000000|B|维吾尔一]',
                        'Data:2015-01-01 12:00:01|000000|B|撒一]','[DataEnd]',
                        'Data:2015-01-01 12:00:01|000000|K|阿斯顿啊个]']
            for i in data:
                print(i)
                connection.sendall(bytes(i,encoding='utf-8'))
                rec_data = connection.recv(BUFSIZ)
                data_str_rec = bytes.decode(rec_data)
                print(data_str_rec)
        elif data_rev ==b'[DataCount]':#测试
            connection.sendall(b'11')
            continue
        elif data_rev ==b'[DataEmpty]':#数据发送完毕 或者   已经清空缓存
            connection.sendall(b'[DataEnd]')
            continue

if __name__ == '__main__':
    Server()
