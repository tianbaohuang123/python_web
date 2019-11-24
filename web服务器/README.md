# web服务器
正则表达式
import re

re.match(正则表达式, 需要处理的字符串)

[], \d, \s, \S, ., \w, \W, {}, ?, +, *

=====================

设定套接字选项：tcp_server_socket.setsockopt(socket.SOL_SOL_SOCKET, socket.SO_REUSEADDR, 1)
将套接字变为非堵塞：tcp_server_socket.setblocking(False)
数据分行：request_lines = request.splitlines()

构造报文数据：

response_body = DATA
response_header = "HTTP/1.1 200 OK\r\n"
response_header += "COntent-Length:%d\r\n" % len(response_body))
response_header += "\r\n"

response = response_header.encoder("utf-8") + response_body

new_socket.send(response)

=====================
epoll实现http
创建epoll对象: epl = select.epoll()
将监听套接字对应的fd注册到epoll中: epl.register(tcp_server_socket.fileno(), select.EPOLLIN)
检测数据: fd_event_list = epl.poll() # 默认堵塞，直到os监测到数据到来 通过事件通知方式 告诉这个程序，此时才会解堵塞
    （fd, event）:fd - 套接字对应的文件描述符，event - 这个文件描述符到底是什么事件



