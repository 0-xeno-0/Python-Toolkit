#!/usr/bin/python3

import socket

host = '192.168.45.244'
port = 8080
BUFF_SIZE = 2024

try:
    server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen(4)
    print("\t\t\t\t\t" + '[++]    ServerLive    [++]' + "\n\n")
    while True:
        # conn = the connected socket and can be used to send & recv data
        conn, addr = server.accept()
        print('[*]Connection Recieved from : ' + str(addr) + "\n" + '[*]On Socket : ' + str(conn))
        senMsg = 'Connection Established' + '\r\n'
        conn.send(senMsg.encode())
        try:
            rcvmsg = conn.recv(BUFF_SIZE)
            print(rcvmsg.decode())
        except ConnectionResetError:
            print('[+]Connection Rest from %s'%str(addr))
            pass
        conn.close()
except KeyboardInterrupt:
    print("\t\t\t\t\t" + '[!!]Server Manual Abort[!!]' + "\n\n")