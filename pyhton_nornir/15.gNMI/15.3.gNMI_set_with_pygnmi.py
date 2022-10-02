#https://github.com/aristanetworks/openmgmt/tree/main/src/pygnmi
from nornir import InitNornir
from pygnmi.client import gNMIclient
from rich import print as rprint

nr = InitNornir(config_file="config.yaml")

u = [
    (
        "openconfig:/interfaces/interface[name=Ethernet1]",
        {"config": {"name": "Ethernet1", "enabled": True, "description": "TestTEST"}},
    )
]


def set_with_pygnmi(task,config):
  with gNMIclient(
    target=(task.host.hostname, task.host.port),
    username=task.host.username,
    password=task.host.password,
    insecure=True) as client:

      result = client.set(update=u)
      rprint(result)

results = nr.run(task=set_with_pygnmi, config=u)
