import socket

def main():
    # 创建一个udp套接字
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    while True:
        # 从键盘获取数据
        send_data = input("请输入要发送的数据:")

        # 如果输入内容是exit，退出
        if "exit" == send_data:
            break

        # 可以使用套接字收发数据
        udp_socket.sendto(send_data.encode("utf-8"), ("192.168.0.117", 8088))

    udp_socket.close()

if "__main__" == __name__:
    main()
