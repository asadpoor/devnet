#https://github.com/aristanetworks/openmgmt/tree/main/src/pygnmi
from nornir import InitNornir
from pygnmi.client import gNMIclient
from rich import print as rprint

nr = InitNornir(config_file="config.yaml")

path1 = ["/interfaces/interface[name=Ethernet1]/config/description"]

def delete_with_pygnmi(task, path):
    with gNMIclient(
      target=(task.host.hostname, task.host.port),
      username=task.host.username,
      password=task.host.password,
      insecure=True) as client:

      response = client.set(delete=path)
      print(respone)

results = nr.run(task=delete_with_pygnmi, path=path1)
