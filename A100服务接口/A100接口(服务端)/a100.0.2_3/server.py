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
# def Server(th):
def Server(thread):
    try:
        connection, address = sock.accept()  # 开始接受请求,进入等待阻塞状态，直到有链接到达
        ok = '[ConnectData]'
        connection.sendall(bytes(ok, encoding='utf-8'))
    except sock.error as e:
        print('conn fail :' % e)
    s_emty = input('是否清空缓冲区数据(Y/N)：')
    if s_emty == 'N':
        while 1:
            data_rev = connection.recv(BUFSIZ)  # 接收客户端发过来的数据  #对data_rev进行解析，是否为所需的正确数据
            #bytes转换 汉字
            data_str = bytes.decode(data_rev)
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
                continue
            elif data_rev ==b'[DataEnd]':#数据发送完毕 或者   已经清空缓存
                data_over = b'dataend!!!!!!!!!!!!!!'
                print(data_over)
                # break
                print('Connect close!')
                sock.close()
    elif s_emty == 'Y':
     #清空缓存
        s_emty_data = '[DataEmpty]'
        connection.sendall(bytes(s_emty_data, encoding='utf-8'))
        # 接收客户端发过来清空数据缓存的消息
        data_end = connection.recv(BUFSIZ)
        print(data_end)
    else:
        print('输入错误！')

if __name__ == '__main__':
    '''
        t1 = threading.Thread(target=sayhi,args=(1,)) #生成一个线程实例
        t2 = threading.Thread(target=sayhi,args=(2,)) #生成另一个线程实例
        t1.start() #启动线程
        t2.start() #启动另一个线程
        print(t1.getName()) #获取线程名
        print(t2.getName())
        t1.join() #t2.wait()
        t2.join() #t2.wait()'''
    # t_list = []  # 定义一个空列表，每启动一个实例，将实例添加到列表
    # for i in range(5):
    #     t = threading.Thread(target=Server, args=[i,])
    #     t_list.append(t)
    # for th in t_list: #循环列表 ，等待列表中的每一个线程执行完毕
    #     th.setDaemon(True)
    #     th.start()
    #     print('启动线程')
    # th.join()

    local_t = threading.local()
    local_t = []
    for i in range(10):
        local_t.append(random.randrange(10))
    # 显示线程的状态，和随机产生的10个数字
    # print(threading.currentThread(), local_t)
    print('主线程开始！')
    for item in range(7):
        t  = Server(item)
        # t.start()
    # t.join()
        # join函数控制线程执行顺序，不要在start之前调用join函数
        # isDaemon函数查看线程后台运行状态
        # print(t.isDaemon())
    print("主线程结束")

    # Server()


    # pp = []
    # p = Pool(3)
    # for i in range(3):
    #     t = p.apply_async(Server, args=(i,))
    #     pp.append(t)
    # for th in pp:
    #     p.close()
    #     p.join()
