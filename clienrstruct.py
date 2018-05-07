#cliend/sender
import socket,struct,sys
message = 'very important data[kamu jomlo yah....]'
multicast_group = ('224.3.29.77', 10001)
#create The datagram socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#set A timeout so the socket does not block indefinelty when trying
#to receive data.
sock.settimeout(0.2)
#set the time-to-live for message to 1 so they do not go past the
#local network segment
ttl = struct.pack('b', 1)
sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, ttl)
try:
    #send data to the multicast group
    print('sending"%s"' %message)
    sent = sock.sendto(message, multicast_group)
    #look for response from all recipients
    while True:
        print('waiting to receive')
        try:
            data, server = sock.recvfrom(16)
        except socket.timeout:
            print('time out, no more response')
            break
        else:
            print('received "%s" from %s' % (data,server))
except:
        print('closing socket')
        sock.close()