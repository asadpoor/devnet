#https://github.com/aristanetworks/openmgmt/tree/main/src/pygnmi
import json
from nornir import InitNornir
from pygnmi.client import gNMIclient
from rich import print as rprint

nr = InitNornir(config_file="config.yaml")

path1 = ["/interfaces/interface[name=Ethernet1]/state/counters/in-octets"]

def get_with_pygnmi(task, path):
  with gNMIclient(
    target=(task.host.hostname, task.host.port),
    username=task.host.username,
    password=task.host.password,
    insecure=True) as client:

      result = client.get(path=path, encoding="json_ietf")
#      rprint(result)
      print(json.dumps(result, sort_keys=True, indent=2))

results = nr.run(task=get_with_pygnmi, path=path1)
