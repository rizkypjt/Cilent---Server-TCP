import requests
import json

url = "http://idx.co.id/umbraco/Surface/Home/GetTopValue?resultCount=10"
reqdata = requests.get(url).json()
recon_data = json.loads(reqdata)

# untuk menampilkan keynya
# for x in recon_data:
#     print(x.keys())

print("Code\tPrice\tVolume\tValue")
for x in recon_data:
     #print("%s %f %d" %(x["Code"],x["Price"],x["Volume"])) #tanpa subjudul
     print("%s %0.2f %d %d" %(x["Code"],x["Price"],x["Volume"],x["Value"]))