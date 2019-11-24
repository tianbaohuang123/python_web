import socket

def send_file_2_client(client_socket, client_addr):
    # 1.接收客户端需要下载的文件名
    file_name = client_socket.recv(1024).decode("utf-8")

    print("客户端%s需要下载文件：%s" % (str(client_addr), file_name))

    # 2.打开这个文件，读取数据
    file_content = None
    try:
        f = open(file_name, "rb")
        file_content = f.read()
        f.close()
    except Exception as ret:
        print("没有要下载的文件（%s）" % file_name)

    # 3.发送文件的数据给客户端
    if file_content:
        client_socket.send(file_content)


def main():
    # 1.创建套接字
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 2.绑定套接字
    tcp_server_socket.bind(("", 8080))

    # 3.监听套接字
    tcp_server_socket.listen(128)

    while True:
        # 4.等待客户端的链接
        client_socket, client_addr = tcp_server_socket.accept()

        # 5.调用发送文件函数，完成客户端服务
        send_file_2_client(client_socket, client_addr)

        client_socket.close()

    tcp_server_socket.close()

if "__main__" == __name__:
    main()