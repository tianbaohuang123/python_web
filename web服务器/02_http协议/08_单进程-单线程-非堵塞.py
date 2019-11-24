import socket
import time

# 1. 创建套接字
tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# 2. 绑定
tcp_server_socket.bind(("", 7890))

# 3. 变为监听套接字
tcp_server_socket.listen(128)

# 4. 设置套接字为非堵塞的方式
tcp_server_socket.setblocking(False)

client_socket_list = list()

while True:
    # 4. 等待新客户端的链接
    try:
        new_socket, client_addr = tcp_server_socket.accept()
    except Exception as ret:
        print("---没有新的客户端到来---")
    else:
        print("---只要没有产生异常，那么也就意味着来了一个新的客户端---")
        new_socket.setblocking(False)
        client_socket_list.append(new_socket)

    # 5. 为这个客户端服务
    for client_socket in client_socket_list:
        # 1.接收浏览器发送过来的请求，即http请求
        try:
            recv_data = client_socket.recv(1024).decode("utf-8")
        except Exception as ret:
            print(ret)
            print("---这个客户端没有发送过来数据---")
        else:
            print("---没有异常---")
            print(recv_data)
            if recv_data:
                # 对方发送了数据
                print("---客户端发送了数据---")
            else:
                # 对方调用close 导致了 recv返回
                client_socket.close()
                client_socket_list.remove(client_socket)
                print("---客户端已经关闭---")

# 关闭客户端
tcp_server_socket.close()
