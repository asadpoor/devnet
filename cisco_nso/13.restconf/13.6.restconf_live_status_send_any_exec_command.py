import requests
import json

url = "http://192.168.2.201:8080/restconf/data/tailf-ncs:devices/device=R1/live-status/tailf-ned-cisco-ios-stats:exec/any"

payload = json.dumps({
  "input": {
    "args": "show ip interface brief"
  }
})
headers = {
  'Accept': 'application/yang-data+json',
  'Content-Type': 'application/yang-data+json',
  'Authorization': 'Basic YWRtaW46YWRtaW4='
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
