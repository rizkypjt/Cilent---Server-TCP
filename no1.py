# import csv
# with open('contoh.csv') as csvfile:

#     readCSV = csv.reader(csvfile, delimiter='=')
#     for row in readCSV:
#         print(row)

# fname = "/etc/group"
# fp = open(fname)
# data = fp.read()
# fp.close()

# cut = data.split(':')
# print(cut)

import urllib2
import threading
urls = ['192.168.1.22','www.detik.com']

class web(threading.Thread):
 def __init__(self,threadName,url):
    threading.Thread.__init__(self)
    self.name = threadName
    self.url = url

 #self.status = "Down"
 def run(self):
    try:
        con = urllib2.urlopen("http://%s"%self.url, timeout=30)
        print("Web %s is Run"%self.url)
        del(con)
    except urllib2.URLError,e:
        print("Oops Web %s is Down"%self.url)
        
y=1
for url in urls:
    t = web('thread-%d'%y,url)
    t.start()
    y += 1
