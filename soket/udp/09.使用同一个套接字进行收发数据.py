import socket

def main():

    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    dest_ip = input("请输入对方ip：")
    dest_port = int(input("请输入对方port："))

    send_data = input("请输入数据：")

    udp_socket.sendto(send_data.encode("utf-8"), (dest_ip, dest_port))

    recv_data = udp_socket.recvfrom(1024)
    print(recv_data[0].decode("gbk"))

    udp_socket.close()

if __name__ == "__main__":
    main()
