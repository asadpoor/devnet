import requests
import json

# manually added
requests.packages.urllib3.disable_warnings()

url = "https://192.168.2.91:443/restconf/data/ietf-interfaces:interfaces"

payload={}
headers = {
  'Content-Type': 'application/yang-data+json',
  'Accept': 'application/yang-data+json',
  'Authorization': 'Basic cmF5a2E6cmF5a2EtY28uY29t'
}

# verify=False is added
response = requests.request("GET", url, headers=headers, data=payload, verify=False)

print(response.text)
