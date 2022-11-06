import socket
s=socket.socket()

host="127.0.0.1"
port=3335

s.bind((host,port))
s.listen(2)

clients=[]

for i in range(2):
    c,addr=s.accept()
    clients.append(c)
    # print(clients)
print(clients)
alice=clients[0]
bob=clients[1]

while True:
    # s.recv(1024).decode()
    msg=s.recv(1024).decode()
    print(msg)

s.close()