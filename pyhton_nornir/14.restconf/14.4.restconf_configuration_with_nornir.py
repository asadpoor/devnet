import requests
import json
from nornir import InitNornir
from rich import print as rprint
from nornir_utils.plugins.functions import print_result

requests.packages.urllib3.disable_warnings()

nr = InitNornir(config_file="config.yaml")

headers = {
    "Accept": "application/yang-data+json",
    "Content-Type": "application/yang-data+json",
}

payload = {
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
                'router-id': '1.1.1.1'
            }
        ]
    }
}

def restconf_configuration_nornir_example(task):

    module = "Cisco-IOS-XE-native:native/router/router-ospf/ospf"
    url = f"https://{task.host.hostname}:443/restconf/data/{module}"
    response = requests.put(url, headers=headers, data=json.dumps(payload), auth=(f"{task.host.username}", f"{task.host.password}"), verify=False)
    print(response)

result = nr.run(task=restconf_configuration_nornir_example)
print_result(result)
