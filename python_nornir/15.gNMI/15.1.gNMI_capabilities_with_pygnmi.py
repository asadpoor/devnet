#https://github.com/aristanetworks/openmgmt/tree/main/src/pygnmi
from pprint import pprint as pp
from nornir import InitNornir
from pygnmi.client import gNMIclient

nr = InitNornir(config_file="config.yaml")

def capabilities_with_pygnmi(task):
  with gNMIclient(
    target=(task.host.hostname, task.host.port),
    username=task.host.username,
    password=task.host.password,
    insecure=True) as client:

      result = client.capabilities()
      pp(result)

results = nr.run(task=capabilities_with_pygnmi)
