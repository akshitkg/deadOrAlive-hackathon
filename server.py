import socket
import os
import sys
print("Server socket created!")
print("Now listening...")
#host=socket.gethostname()
host="127.0.0.1"
port=12000 #ports after 6000 are free
s=socket.create_server((host,port))
# print(s)
# s.bind((host,port))
s.listen(10)
while True:
    c,addr=s.accept()
    print( "Client connected: ",addr)
    # print("Got Connection from: " ,addr)
    content=c.recv(100).decode()
    if not content:
        break
    print(content) 