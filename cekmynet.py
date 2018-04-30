
import os


pattern = "3 received"
nets = "192.168.6."
ips = range(1,255)

for x in ips :
	ipx = nets + str(x)
	cmd = "ping -q -c3 %s" %(ipx)
	fp = os.popen(cmd)
	outx = fp.read()
	if outx.find(pattern) > -1:
		status = "Up"

	print("Host %s is %s" %(ipx,status))
	status = "Down"
