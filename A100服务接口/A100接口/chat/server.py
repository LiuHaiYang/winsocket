# coding=utf-8
import socket
# Server
def Server():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('localhost', 8000))
    sock.listen(5)  # 监听，最大链接数
    while 1:
        print('Wait Connecting...')
        connection, address = sock.accept()  # 开始接受请求,进入等待阻塞状态，直到有链接到达
        print('Connect OK!')
        while 1:
            data = connection.recv(1024)  # 接收客户端发过来的数据
            if not data:
                break
            # print('client >>> ' + bytes(data,encoding='utf-8'))
            print(b'client :'+data)
            s_ipt = input('Server >>> ')
            if s_ipt == 'bye':
                connection.close()
            connection.sendall(bytes(s_ipt,encoding='utf-8'))  # 发送数据到客户端，即上面到connection
if __name__ == '__main__':
    Server()