import json
import requests
from nornir import InitNornir
from rich import print as rprint

requests.packages.urllib3.disable_warnings()

nr = InitNornir(config_file="config.yaml")

header1 = {"Accept": "application/yang-data+json"}


def restconf_nornir_example(task):
    url = f"https://{task.host.hostname}:443/restconf/data/Cisco-IOS-XE-native:native/router/router-ospf"
#    url = f"https://{task.host.hostname}:443/restconf/data/Cisco-IOS-XE-native:native/router/bgp"
    response = requests.get(url=url, headers=header1, auth=(f"{task.host.username}", f"{task.host.password}"), verify=False)
    rprint(response.json())

# to copy configuratio of each network device in a variable with it's name and "data" key
    task.host["data"] = response.json()

# to process dictionary
#    result = task.host["data"]["Cisco-IOS-XE-ospf:router-ospf"]
#    result = task.host["data"]["Cisco-IOS-XE-ospf:router-ospf"]["ospf"]
    result = task.host["data"]["Cisco-IOS-XE-ospf:router-ospf"]["ospf"]["process-id"]
    rprint(result)

# to search in list structure
    for ospf_process_id in task.host["data"]["Cisco-IOS-XE-ospf:router-ospf"]["ospf"]["process-id"]:
      rprint("ospf pricess id = ", ospf_process_id["id"])
      for network_ in ospf_process_id["network"]:
        rprint("network = ", network_)

# dictionary parsing
#    for key, value in result.items():
#      print("key=", key)
#      print("value=", value)


# list parsing
#    for ospf_process_id in result:
#      print(ospf_process_id["router-id"])


nr.run(task=restconf_nornir_example)

