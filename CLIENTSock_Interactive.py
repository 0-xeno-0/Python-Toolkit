#!/usr/bin/python3

import socket
import telnetlib

host = socket.gethostname
port = 8080
BUFF_SIZE = 1024

def interSocket(socket):
    t =telnetlib.Telnet()
    t.sock = socket
    t.interact()

def transFormat(msg):
    senChoice = input('[?]Do you want to send the recieved message? Please specify the format [Decoded(D) / Encoded(E)]: ').strip()
    if senChoice == 'D' or senChoice == 'd':
        return msg.decode()
    elif senChoice == 'E' or senChoice == 'e':
        return msg.encode()

def clientSocket():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((host,port))
    recMsg = client.recv(BUFF_SIZE)
    print (recMsg.decode)
    senMsg = input('[!]Message to send the server: ').strip()
    if len(senMsg) == 0:
         tf = transFormat(recMsg)
         client.send(tf)
    elif  len(senMsg) != 0:
        client.send(senMsg.encode())
    interSocket(client)
    client.close()
    return recMsg

try:
    connTest = clientSocket()
    if(len(connTest)==0):
        print('Reconnecting to Server : ....')
        while(len(connTest)==0):
            print('[+]Reconnecting -->... ')
            connTest = clientSocket()
except ConnectionRefusedError:
    print('[***]Connecting Refused[***]')
    exit(1)