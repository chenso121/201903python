import socket

# 1. 创建服务端socket对象
server = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)

# 2. 绑定地址和端口(IP:port)
server.bind(('0.0.0.0', 9995))

# 3. 监听是否有客户端连接?listen
server.listen(5)
print('server start .........')
# 4.接收客户端的连接accept
clientSocketObj, clientAddress = server.accept()
while True:
    # 5. 接收客户端发送的消息
    recv_data = clientSocketObj.recv(1024).decode('utf-8')
    print("接收到客户端发送的消息:", recv_data)
    if recv_data == 'quit':
        break
    # 6. 给客户端发送消息
    send_data = input('server:>> ').encode('utf-8')
    if not send_data:
        continue
    clientSocketObj.send(send_data)

# 7. 关闭socket对象
clientSocketObj.close()
server.close()
