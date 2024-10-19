#https://blog.wimwauters.com/networkprogrammability/2020-04-04_restconf_python/

import requests
import json
from rich import print as rprint

requests.packages.urllib3.disable_warnings()

HOST = "192.168.1.11"
PORT = "443"
USER = "rayka"
PASSWORD = "rayka-co.ir"

headers = {
      "Accept" : "application/yang-data+json", 
      "Content-Type" : "application/yang-data+json", 
   }

#module = "ietf-interfaces:interfaces"
module = "Cisco-IOS-XE-native:native/router/router-ospf/ospf"
url = f"https://{HOST}:{PORT}/restconf/data/{module}"

payload = {
        'interface': [
            {
                'name': 'Loopback112',
                'type': 'iana-if-type:softwareLoopback',
                'enabled': True,
                'ietf-ip:ipv4': {'address': [{'ip': '192.168.112.11', 'netmask': '255.255.255.0'}]},
                'ietf-ip:ipv6': {}
            }
        ]
}

payload1 = {
        'process-id': [
            {
                'id': 1,
                'network': [
                    {'ip': '192.168.12.0', 'wildcard': '0.0.0.255', 'area': 0},
                    {'ip': '192.168.13.0', 'wildcard': '0.0.0.255', 'area': 1},
                    {'ip': '192.168.14.0', 'wildcard': '0.0.0.255', 'area': 1},
                    {'ip': '192.168.111.0', 'wildcard': '0.0.0.255', 'area': 0}
                ],
                'router-id': '1.1.1.1'
            }
        ]
}

payload2 = {
    'Cisco-IOS-XE-ospf:ospf': {
        'process-id': [
            {
                'id': 1,
                'network': [
                    {'ip': '192.168.12.0', 'wildcard': '0.0.0.255', 'area': 0},
                    {'ip': '192.168.13.0', 'wildcard': '0.0.0.255', 'area': 1},
                    {'ip': '192.168.14.0', 'wildcard': '0.0.0.255', 'area': 1},
                    {'ip': '192.168.111.0', 'wildcard': '0.0.0.255', 'area': 0}
                ],
                'router-id': '11.11.11.11'
            }
        ]
    }
}

#response = requests.get(url, headers=headers, auth=(USER, PASSWORD), verify=False).json()
#response = requests.post(url, headers=headers, data=json.dumps(payload), auth=(USER, PASSWORD), verify=False)
#response = requests.post(url, headers=headers, data=json.dumps(payload1), auth=(USER, PASSWORD), verify=False)
#response = requests.put(url, headers=headers, data=json.dumps(payload2), auth=(USER, PASSWORD), verify=False)

url = f"https://{HOST}:{PORT}/restconf/data/{module}/process-id=1"
response = requests.delete(url, headers=headers, auth=(USER, PASSWORD), verify=False)

rprint(response)
#print(response)
#pprint(response)
