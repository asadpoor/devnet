import requests
import json

HOST = "192.168.2.101"
PORT = "8080"
USER = "admin"
PASSWORD = "admin"

url = f"http://{HOST}:{PORT}/restconf/data/tailf-ncs:devices/device=R1/live-status/tailf-ned-cisco-ios-stats:exec/any"

payload = json.dumps({
  "input": {
    "args": "show ip interface brief"
  }
})
headers = {
  'Accept': 'application/yang-data+json',
  'Content-Type': 'application/yang-data+json',
}

response = requests.request("POST", url, headers=headers, auth=(USER, PASSWORD), data=payload)

print(response.text)
