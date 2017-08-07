import  socketserver
# 服务端
HOST='127.0.0.1'
POST=20001
BUFSIZ=1024
class Myserver(socketserver.BaseRequestHandler):
    def Connect(self):
        connection = self.request
        while 1:
            print('ok!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
            ok = '[ConnectData]'
            connection.sendall(bytes(ok, encoding='utf-8'))
        return connection
    def Rec(self):
        conn = Myserver.Connect()
        data_rev = conn.recv(BUFSIZ)  # 接收客户端发过来的数据  #对data_rev进行解析，是否为所需的正确数据
        # if  re.match(r'\w\w\d',data_rev):#数据
        if data_rev != ' ':  # 数据
            data = data_rev
            ok = b'aa3'
            if data == ok:  # 正确的数据
                data_ok = '[DataOK]'
                conn.sendall(bytes(data_ok, encoding='utf-8'))
            elif data != ok:  # 不正确数据
                data_fail = '[DataFail]'
                conn.sendall(bytes(data_fail, encoding='utf-8'))
            else:
                pass
        elif data_rev ==b'[DataEnd]':
            pass
        else:
            pass
        return data_rev
    def Test(self):
        conn = Myserver.Connect()
        test = Myserver.Rec()
        if test ==b'[DataTest]':
            conn.sendall(b'TestOK')
        print(b'OK')
    def Emty(self):
        conn = Myserver.Connect()
        s_emty = b'[DataEmty]'
        conn.sendall(bytes(s_emty, encoding='utf-8'))
        data_emty = conn.recv(BUFSIZ)  # 接收客户端发过来清空数据缓存的消息
        print(data_emty)
    # Connect()
    # Rec()
    # Test()
    # Emty()
if __name__ == "__main__":
    server = socketserver.ThreadingTCPServer((HOST,POST),Myserver)
    server.serve_forever()