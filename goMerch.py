import json
import requests
from datetime import datetime
from datetime import date
#pip3 install dnsdumpster
from dnsdumpster.DNSDumpsterAPI import DNSDumpsterAPI

target = 'midtrans.com'

#waktu
waktu = datetime.now()
waktu = waktu.strftime("%H:%M:%S")

def myconverter(o):
    if isinstance(o,  (datetime, date)):
        return o.__str__()

#tanggal
tanggal = date.today()



#shodan
url = "https://api.shodan.io/shodan/host/search?key=XJVYkVG85D1yzlcD3MBre7scENsg1rE3&query="+target+"&facets=ssl.cipher.version"

response = requests.request("GET", url)
response = response.content
response = json.loads(response)
for id in response["matches"]:
    host = (id["http"]["host"])
    # print ("host\t: "+host)
    port = (id["port"])
    # print ("port\t: "+str(port))
    try:
        chiper = (id["ssl"]["cipher"]["version"])
        # print ("ssl chiper\t: "+chiper)
    except:
        pass


#DNS DUMPSTER
results = DNSDumpsterAPI().search(target)
domain = results["domain"]
results = results["dns_records"]
data =[]
for id in results["host"]:
    item ={"subdomain":id["domain"],
    "ip address" :id["ip"]}
    data.append(item)
jsonData=data


#SecurityTrails
url = "https://api.securitytrails.com/v1/domain/"+target
url_sub = "https://api.securitytrails.com/v1/domain/"+target+"/subdomains"
querystring = {"apikey":"589MZT3zFGjUUuAyR4ZkvbwqcxUgTXKl"}

#domain
response = requests.request("GET", url, params=querystring)
response = json.loads(response.text)
hostname = response["hostname"]
# print("domain\t: "+hostname)
response = response["current_dns"]["a"]["values"][0]["ip"]
# print ("ip address\t: "+response)

#subdomain
response_sub = requests.request("GET", url_sub, params=querystring)
response_sub = json.loads(response_sub.text)
response_sub = response_sub["subdomains"]



#censys.io
API_URL = "https://censys.io/api/v1/view/websites/"+target
UID = "e717e046-134f-40ab-9d0d-81c7ffdc823b"
SECRET = "t6wPtPeZYkWm18zVyebNpYzraNfdHFQA"

res = requests.get(API_URL, target, auth=(UID, SECRET))
res = res.content
res = json.loads(res)
domain = res["domain"]
protocol = res["protocols"]


output = {"waktu":waktu,
"tanggal":tanggal,
"data":[{
    "shodan":[
    {"host":host,
    "port":port,
    "ssl chiper":chiper
    }],
    "SecurityTrails":[{
        "hostname":hostname,
        "response":response
    },
    {"subdomain":response_sub}
    ],
    "censys":[{
        "domain":domain,
        "protocol":protocol
    }],
    "dnsdumpster":[{
        "domain":domain,
        "subdomain":jsonData
    }]}]
    }

print(json.dumps(output, indent=2, default=myconverter))
