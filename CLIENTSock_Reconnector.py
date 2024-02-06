#!/usr/bin/python3

import socket

host = '192.168.185.68'
port = 2001
BUFF_SIZE = 1024

def clientSocket():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((host,port))
    recMsg = client.recv(BUFF_SIZE)
    print ('[!]Recieved : ' + recMsg.decode())
    senMsg = client.send(recMsg)
    print ('[$] Sent : ' + str(senMsg))
    client.close()
    return recMsg

for i in range(11):
    print(i)
    try:
        try:
            connTest = clientSocket()
            if(len(connTest)==0):
                print('[Reconnecting to Server]')
                while(len(connTest)==0):
                    print('[+]Reconnecting -->... ')
                    connTest = clientSocket()
        except OSError:
            pass
    except ConnectionRefusedError:
        print('...[*]Connecting Refused[*]...')
        exit(1)