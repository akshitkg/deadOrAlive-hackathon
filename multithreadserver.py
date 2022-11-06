import socket
import os
from _thread import *
ServerSideSocket = socket.socket()
host = '127.0.0.1'
port = 2007
ThreadCount = 0
data=["null","null"]
try:
    ServerSideSocket.bind((host, port))
except socket.error as e:
    print(str(e))
print('Socket is listening..')
ServerSideSocket.listen(5)
def multi_threaded_client(connection,thread_number):
    
    connection.send(str.encode('Server is working:'))
    
    while True:

        data[thread_number] = connection.recv(2048).decode()
        response = 'Server message: ' + data[1-thread_number]
        if not data:
            break
        connection.send(str.encode(response))
    connection.close()
while True:
    Client, address = ServerSideSocket.accept()
    print('Connected to: ' + address[0] + ':' + str(address[1]))
    start_new_thread(multi_threaded_client, (Client, ThreadCount, ))
    ThreadCount += 1
    print('Thread Number: ' + str(ThreadCount))
ServerSideSocket.close()