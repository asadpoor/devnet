import requests
import json

url = "http://192.168.2.201:8080/restconf/data/tailf-ncs:devices/device=R1/config/tailf-ned-cisco-ios:interface/"

payload = json.dumps({
  "Loopback": [
    {
      "name": "300",
      "ip": {
        "address": {
          "primary": {
            "address": "4.5.16.17",
            "mask": "255.255.255.255"
          }
        }
      }
    }
  ]
})
headers = {
  'Authorization': 'Basic YWRtaW46YWRtaW4=',
  'Accept': 'application/yang-data+json',
  'Content-Type': 'application/yang-data+json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
