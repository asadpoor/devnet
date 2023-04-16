import requests
import json

url = "http://192.168.2.201:8080/restconf/data/tailf-ncs:devices/device=R1/config/tailf-ned-cisco-ios:interface/Loopback=300"

payload={}
headers = {
  'Content-Type': 'application/yang-data+json',
  'Accept': 'application/yang-data+json',
  'Authorization': 'Basic YWRtaW46YWRtaW4='
}

response = requests.request("DELETE", url, headers=headers, data=payload)

print(response.text)
