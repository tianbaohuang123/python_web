import socket

def main():
    # 1.创建套接字
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
   
    # 2.绑定一个本地信息
    localaddr = ("", 7788)
    udp_socket.bind(localaddr)

    while True:
        # 3.接收数据
        # 接收到的数据是一个元祖(接收到的数据, (发送方的ip, port))
        recv_data = udp_socket.recvfrom(1024) 

        recv_msg = recv_data[0]
        send_addr = recv_data[1]

        # 4.打印接收到的数据
        print("%s:%s" % (str(send_addr), recv_msg.decode("gbk")))

    # 5.关闭套接字
    udp_socket.close()

if __name__ == "__main__":
    main()
