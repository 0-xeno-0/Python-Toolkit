#!/usr/bin/python3

import socket
import sys

host = socket.gethostname()
port = 8080
BUFF_SIZE = 1024
# file_path = /home/xeno/Downloads

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((host, port))

payload = b''
i = 0

while True:
    data = sock.recv(BUFF_SIZE)
    if data:
        payload += data
        i = i + 1
    else:
        print("No data received")
        break

print(len(payload))

def receive_data(server_ip, server_port, buffer_size=1024):
    # Connect to the server
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((server_ip, server_port))

    # Receive data in chunks
    received_data = b''
    while True:
        chunk = sock.recv(buffer_size)
        if chunk:
            received_data += chunk
        else:
            break

    return received_data

def save_data_to_file(data, file_path):
    with open(file_path, 'wb') as f:
        f.write(data)

if __name__ == "__main__":
    server_ip = host
    server_port = port
    data = receive_data(server_ip, server_port)
    
    file_path = 'received_data.txt'
    save_data_to_file(data, file_path)
    print(f"Received data saved to {file_path}")

imageArray = payload.split(b'\r\n\r\n')

for i in range(0, len(imageArray) - 1):
    pos = imageArray[i].find(b'\r\n')
    fileName = b'fetched_' + imageArray[i][0:pos]
    print(fileName.decode())
    fileContent = imageArray[i][pos + 2:-2]

    with open(fileName.decode(), 'wb+') as f:
        f.write(fileContent)