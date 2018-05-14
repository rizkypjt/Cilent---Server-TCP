import requests
import json
url = "http://idx.co.id/umbraco/Surface/Home/GetTopValue?resultCount=10"
reqdata = requests.get(url).json()
recon_data = json.loads(reqdata)

f = file("hasil.CSV","a")
f.write("Code,Price,Volume,Value\n")

for x in recon_data:
    f.write("%s,%0.2f,%d,%d\n" %(x["Code"],x["Price"],x["Volume"],x["Value"]))

f.close()