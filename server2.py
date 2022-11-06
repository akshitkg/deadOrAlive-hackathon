import socket
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

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
    try:
        msg=s.recv(1024).decode()
        
        print(msg)
        if (msg.startswith("1")):
            bob.send(msg[2:].encode())
        if (msg.startswith("2")):
            alice.send(msg[2:].encode())
            print(msg)
    except:
        continue

s.close()