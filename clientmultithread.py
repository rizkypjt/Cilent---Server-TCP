from socket import socket, AF_INET, SOCK_STREAM
(SERVER, PORT) = ('127.0.0.1', 9999)
s = socket(AF_INET, SOCK_STREAM)
s.connect((SERVER, PORT))
pesan = raw_input("Pesan Anda :")
s.send(pesan)
data = s.recv(1024)
s.close()
print 'Received', data