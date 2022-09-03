#https://<ADDRESS>/<ROOT>/data/<[YANG MODULE:]CONTAINER>/<LEAF>[?<OPTIONS>]

#Some notes:

#ADDRESS - The IP (or DNS Name) and Port where the RESTCONF agent is available.
#ROOT - The main entry point for RESTCONF requests.
#Before connecting to a RESTCONF server, you must determine the root.
#Per the RESTCONF standard, devices should expose a resource called /.well-known/host-meta to enable discovery of root programmatically.
#data - The RESTCONF API resource type for data
#The "operations" resource type is used to access RPC operations is also available.
#[YANG MODULE:]CONTAINER - The base model container being used.
#Inclusion of the module name is optional.
#LEAF - An individual element from within the container.
#[?\<OPTIONS>] - Some network devices may support options sent as query parameters that impact returned results.
#These options are NOT required and can be omitted.
#Example options
#depth=unbounded: Follow nested models to end. Integer also supported.
#content=[all, config, nonconfig]: Query option controls type of data returned. Default is all.
#fields=expr: Limit what leafs are returned.


import requests
import xmltodict
from rich import print as rprint

requests.packages.urllib3.disable_warnings()

HOST = "192.168.1.11"
PORT = "443"
USER = "rayka"
PASSWORD = "rayka-co.ir"

header1 = {"Accept": "application/yang-data+xml"}
header2 = {"Accept": "application/yang-data+json"}

url1 = f"https://{HOST}:{PORT}/restconf/data/Cisco-IOS-XE-native:native"
url2 = f"https://{HOST}:{PORT}/restconf/data/Cisco-IOS-XE-native:native/ip/domain"

url3 = f"https://{HOST}:{PORT}/restconf/data/Cisco-IOS-XE-native:native/router"
url4 = f"https://{HOST}:{PORT}/restconf/data/Cisco-IOS-XE-native:native/router/router-ospf"
url5 = f"https://{HOST}:{PORT}/restconf/data/Cisco-IOS-XE-native:native/router/router-ospf/ospf"
url6 = f"https://{HOST}:{PORT}/restconf/data/Cisco-IOS-XE-native:native/router/router-ospf/ospf/process-id"
url7 = f"https://{HOST}:{PORT}/restconf/data/Cisco-IOS-XE-native:native/router/router-ospf/ospf/process-id=1"

url75 = f"https://{HOST}:{PORT}/restconf/data/Cisco-IOS-XE-interfaces-oper:interfaces"
url8 = f"https://{HOST}:{PORT}/restconf/data/Cisco-IOS-XE-interfaces-oper:interfaces/interface=GigabitEthernet1"

url9 = f"https://{HOST}:{PORT}/restconf/data/openconfig-interfaces:interfaces?content=config"
url10 = f"https://{HOST}:{PORT}/restconf/data/openconfig-interfaces:interfaces?content=nonconfig"


url11 = f"https://{HOST}:{PORT}/restconf/data/openconfig-interfaces:interfaces/interface=GigabitEthernet1?content=nonconfig"

url12 = f"https://{HOST}:{PORT}/restconf/data/Cisco-IOS-XE-native:native/router/bgp"

url13 = f"https://{HOST}:{PORT}/restconf/data/Cisco-IOS-XE-native:native/ntp"

url14 = f"https://{HOST}:{PORT}/restconf/data/Cisco-IOS-XE-native:native/ip/access-list/Cisco-IOS-XE-acl:extended"

url15 = f"https://{HOST}:{PORT}/restconf/data/openconfig-acl:acl?content=config"

response = requests.get(url=url12, headers=header2, auth=(USER, PASSWORD), verify=False)

# print result inf the format of text or original format
#rprint(response.text)
#rprint(response.content)

# if the result is in the content of xml
#xml_response = response.content
#dic_response = xmltodict.parse(xml_response)
#rprint(dic_response)

# if the result is in the content of json
#rprint(response.json())


dic_response=response.json()
#print(type(dic_response))
#dic_response=dic_response["openconfig-interfaces:interface"]
#dic_response=dic_response["openconfig-interfaces:interface"]["state"]["counters"]
#for  key,value in dic_response.items():
#  print("key=",key)
#  print("value=",value)

rprint(dic_response)
