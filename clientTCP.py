#CLIENT
from socket import socket, AF_INET, SOCK_STREAM
(SERVER, PORT) = ('192.168.10.47', 9999)
s = socket(AF_INET, SOCK_STREAM)
s.connect((SERVER, PORT))
pesan = raw_input('Command : ')
s.send(pesan)
data = s.recv(1024)
s.close()
print('Received: ', data)