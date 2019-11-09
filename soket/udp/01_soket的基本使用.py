import socket

def main():
    # 创建一个udp套接字
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    udp_socket.sendto(b"hello~", ("192.168.0.117", 8080))

    udp_socket.close()

if "__main__" == __name__:
    main()
