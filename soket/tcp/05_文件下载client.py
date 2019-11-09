import socket

def main():
    # 1.创建tcp的套接字
    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 2.链接服务器
    server_ip = input("请输入要连接的服务器的IP：")
    server_port = int(input("请输入要连接的服务器的PORT："))
    server_addr = (server_ip, server_port)

    tcp_socket.connect(server_addr)

    # 3.获取要下载的文件名
    download_file_name = input("请输入要下载的文件名：")

    # 4.将文件名发送给服务器
    tcp_socket.send(download_file_name.encode("utf-8"))

    # 5.接收文件中的数据
    recv_data = tcp_socket.recv(1024)

    if recv_data:
        # 6.保存接收文件到一个文件中
        with open("new_" + download_file_name, "wb") as f:
            f.write(recv_data)

    # 7.关闭套接字
    tcp_socket.close()

if "__main__" == __name__:
    main()