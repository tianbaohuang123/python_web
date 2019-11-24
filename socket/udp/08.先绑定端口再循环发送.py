import socket

def main():
    # 1.创建套接字
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
   
    # 2.绑定一个本地信息
    localaddr = ("", 7788)
    udp_socket.bind(localaddr)

    while True:
        # 3.从键盘获取数据
        send_data = input("请输入数据：")

        # 4.发送数据
        udp_socket.sendto(send_data.encode("utf-8"), ("192.168.0.117", 8088))

    # 5.关闭套接字
    udp_socket.close()

if __name__ == "__main__":
    main()
