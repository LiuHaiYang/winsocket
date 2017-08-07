# codinf=utf-8
import socket
import re
import  pymongo
import time
SERVERHOST='127.0.0.1'
SERVERPORT=20001
DBHOST = '127.0.0.1'
DBPORT = 27017
BUFSIZ=1024
# 超时设置
# timeout = 40
# socket.setdefaulttimeout(timeout)
re1 = '(\\[)'  # Any Single Character 1
re2 = '((?:[a-z][a-z]+))'  # Word 1
re3 = '(:)'  # Any Single Character 2
re4 = '((?:2|1)\\d{3}(?:-|\\/)(?:(?:0[1-9])|(?:1[0-2]))(?:-|\\/)(?:(?:0[1-9])|(?:[1-2][0-9])|(?:3[0-1]))(?:T|\\s)(?:(?:[0-1][0-9])|(?:2[0-3])):(?:[0-5][0-9]):(?:[0-5][0-9]))'  # Time Stamp 1
re5 = '(\\|)'  # Any Single Character 3
re6 = '([a-z])'  # Any Single Word Character (Not Whitespace) 1
re7 = '([\u4e00-\u9fa5]{2,})'
re8 = '(\\])'  # Any Single Character 4
re9 = '([0-9]{6})'
rg = re.compile(re1 + re2 + re3 + re4 + re5 + re9 + re5 + re6 + re5 + re7 + re8, re.IGNORECASE | re.DOTALL)
def Client():

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((SERVERHOST, SERVERPORT))  # 链接服务器
    conn_ok = sock.recv(BUFSIZ)
    conn = bytes.decode(conn_ok)
    print(conn)
    while 1:
        start_i = input('请输入指定操作:(data/count/empty):')
        if start_i == 'data':
            data_f = '[DataFirst]'
            sock.sendall(bytes(data_f, encoding='utf-8'))
            while 1:
                data_rev =  sock.recv(BUFSIZ)
                data = bytes.decode(data_rev)
                if data == '[DataEnd]':
                    print('DataEnd!!!!!!!!!!!!!!!!!!!!!!!!!!')
                elif re.match(rg,data):#对接收的数据进行检验  并 存储
                    print(data)
                    insert(data)
                    data_n = '[DataNext]'
                    print('===========================')
                    sock.sendall(bytes(data_n, encoding='utf-8'))
                else:
                    sock.sendall(bytes(data_f, encoding='utf-8'))

        elif start_i == 'count':
            data_c = '[DataCount]'
            sock.sendall(bytes(data_c, encoding='utf-8'))
            data_count = sock.recv(BUFSIZ)
            print(data_count)
        elif start_i == 'empty':
            data_e = '[DataEmpty]'
            sock.sendall(bytes(data_e, encoding='utf-8'))
            data_empty = sock.recv(BUFSIZ)
            print(data_empty)
        else:
            print('指令出错！')
            continue
def insert(data_rec):
    data = data_zidian(data_rec)
    client_db = pymongo.MongoClient(DBHOST, DBPORT)
    db = client_db.A100_test
    collection = db.a100
    collection.insert(data)


def data_zidian(data_rec):
    ii = []
    for i in data_rec.split('|'):
        ii.append(i)
    # k = ii[0].split(':')[1:]
    #	print(k)
    time_t = ii[0][6:]
    adress = ii[3][:-1]
    # print(ii)
    data = {
        "time": time_t,
        "id": ii[1],
        "name": ii[2],
        "adress": adress
    }
    return data

if __name__ == '__main__':
    Client()