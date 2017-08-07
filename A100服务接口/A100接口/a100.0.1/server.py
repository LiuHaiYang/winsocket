import  socketserver
# 服务端
HOST = '127.0.0.1'
PORT = 8080
BUFSIZE = 1024
ADDR = (HOST, PORT)
class Server(socketserver.BaseRequestHandler):
    #连接
    def Connect(self):
        conn = self.request
        print(b'hello')
        conn.sendall(b"[ConnectOK]", encoding="utf-8")
        conn.recv(BUFSIZE)
    # #接收数据data
    # def Rec(self):
    #     rec_conn=Server.Connect.conn
    #     ret_bytes = rec_conn.recv(BUFSIZE)
        ret_bytes = conn.recv(BUFSIZE)
        ret_str = str(ret_bytes,encoding="utf-8")
        if ret_str == "q":
            # rec_conn.sendall(bytes("DataOK",encoding="utf-8"))
            conn.sendall(bytes("DataOK",encoding="utf-8"))
        else:
            # rec_conn.sendall(bytes("DataFail", encoding="utf-8"))
            conn.sendall(bytes("DataFail", encoding="utf-8"))
    #心跳测试
    def Heart(self):
        pass
    #清空缓存
    def emty(self):
        pass
if __name__ == "__main__":
    server = socketserver.ThreadingTCPServer(ADDR,Server)
    server.serve_forever()