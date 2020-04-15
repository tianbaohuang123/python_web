# socket

# udp:
* 1、创建udp套接字

```python
udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
```

* 2、绑定本地信息

```python
udp_socket.bind(("", PORT))
```

* 3、发送数据

```python
udp_socket.sendto(b"DATA", ("IP", PORT))
```

* 4、接收数据

```python
recv_data = udp_socket.recvfrom(1024)
```

* 5、关闭套接字

```python
udp_socket.close()
```

# tcp:
* 1、创建tcp套接字

```python
tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
```

* 2、链接服务器(客户端)

```python
tcp_socket.connect(("IP", PORT))
```

* 2、绑定本地信息

```python
tcp_server_socket.bind(("", PORT))
```

* 3、监听套接字

```python
tcp_server_socket.listen(128)
```

* 4、等待客户端的链接

```python
new_client_socket, client_addr = tcp_server_socket.accept()
```

* 4、发送数据

```python
new_client_socket.send(send_data.encode("utf-8))
```

* 5、接收数据

```python
recv_data = new_client_socket.recv(1024)
```

* 6、关闭套接字

```python
socket.close()
```
