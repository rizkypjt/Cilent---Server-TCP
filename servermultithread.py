#server dg multithread
from socket import socket, AF_INET, SOCK_STREAM, SOL_SOCKET,SO_REUSEADDR
import threading
s = socket(AF_INET, SOCK_STREAM)
s.setsockopt(SOL_SOCKET,SO_REUSEADDR, 1)
s.bind(('', 9999))
s.listen(5) #max queued Connections
def handle_client(connection, addr):
    try:
        while True:
            data = connection.recv(1024)
            if not data:
                break
            connection.send("HI %s, your message is'%s'"%(addr,data.upper()))
        connection.close()
    except:
        pass
while True:
    connection, addr = s.accept()
    print("Connections from %s accepted..."%str(addr))
    #setiap Client di buatkan thread masing - masing
    t = threading.Thread(target=handle_client,args=[connection,addr])
    t.start()
c.close()