from socket import socket, AF_INET, SOCK_DGRAM
s = socket(AF_INET, SOCK_DGRAM)
s.bind(('10.0.0.2', 0))
print "using", s.getsockname()
server = ('10.0.0.1', 1111)
s.sendto("ini dari aku", server)
data, addr = s.recvfrom(1024)
print "received", data, "from", addr
s.close()