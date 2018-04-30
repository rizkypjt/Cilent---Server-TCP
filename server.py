from socket import socket, AF_INET, SOCK_STREAM
import os
s = socket(AF_INET, SOCK_STREAM)
s.bind(('127.0.0.1 ', 9999))
s.listen(5) #max Quend Connections
cmds = {'mdir':'mkdir','ddir':'rm -rf','rdir':'mv' }
while True:
    sock, addr = s.accept()
    print("Connection From %s Accepted.."%str(addr))
    data = sock.recv(1024)
    if not data:
        continue
    pesan = data.split()
    msg = "failed"
    try:
        if len(pesan) == 2:
            res = os.system(cmds[pesan[0]] + " /tmp/" + pesan[1])
        elif pesan[0] == 'rdir' and len(pesan) == 3:
            res = os.system(cmds[pesan[0]] + " /tmp/" + pesan[2])
        else:
            sock.send("uknown Command...")
            continue
        if res == 0 :
            msg = "succes"
        sock.send(msg+":command have been execute")
    except:
            sock.send("Nothing todo..")