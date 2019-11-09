import socket

def main():
    # 1.创建tcp的套接字（买个手机）
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 2.绑定本地信息
    tcp_server_socket.bind(("", 8080))

    # 3.让默认的套接字由主动变为被动 listen（将手机设置为正常的响铃模式）
    tcp_server_socket.listen(128)

    while True:
        # 4.等待客户端的链接 accept（等待别人的电话到来）
        new_client_socket, client_addr = tcp_server_socket.accept()
        print("一个新的客户端已经到来%s" % str(client_addr))

        while True:
            # 5.接收客户端发送过来的请求
            recv_data = new_client_socket.recv(1024)
            print("客户端发送过来的请求是%s" % recv_data.decode("utf-8"))

            if recv_data:
                # 6.回送一部分数据给客户端
                new_client_socket.send("hhhh".encode("utf-8"))
            else:
                break;

        # 7.关闭客户端套接字
        new_client_socket.close()
        print("已经服务完毕。。。")

    # 8.关闭客户端套接字
    tcp_server_socket.close()

if "__main__" == __name__:
    main()