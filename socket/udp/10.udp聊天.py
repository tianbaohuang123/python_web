import socket

def send_msg(udp_socket):
    dest_ip = input("请输入对方ip：")
    dest_port = int(input("请输入对方port："))

    send_data = input("请输入数据：")

    udp_socket.sendto(send_data.encode("utf-8"), (dest_ip, dest_port))

def recv_msg(udp_socket):
    recv_data = udp_socket.recvfrom(1024)
    print(recv_data[0].decode("gbk"))

def main():

    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    udp_socket.bind(("", 7788))

    while True:
        send_msg()
        recv_msg()

if __name__ == "__main__":
    main()
