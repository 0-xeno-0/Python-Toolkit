#!/usr/bin/python3

import socket

remote_host = 'www.megacorpone.com'
remote_port = 8080
buff_size = 1024

request = 'Get / HTTP/1.1\r\nHost: %s\r\n\r\n' %remote_host
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((remote_host, remote_port))

web_server_response = client.recv(buff_size)
print(web_server_response.decode())
