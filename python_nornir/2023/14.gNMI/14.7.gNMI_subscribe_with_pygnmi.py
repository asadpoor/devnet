#https://github.com/aristanetworks/openmgmt/tree/main/src/pygnmi
from nornir import InitNornir
from pygnmi.client import gNMIclient, telemetryParser

nr = InitNornir(config_file="config.yaml")

subscribe1 = {
    'subscription': [
      {
        'path': 'interfaces/interface[name=Ethernet1]/state/counters/in-octets',
        'mode': 'sample',
        'sample_interval': 10000000000
      },
      {
        'path': '/interfaces/interface[name=Ethernet1]/state/oper-status',
        'mode': 'on_change',
      },
    ],
    'mode': 'stream',
    'encoding': 'json'
}

def subscribe_with_pygnmi(task):
  with gNMIclient(
    target=(task.host.hostname, task.host.port),
    username=task.host.username,
    password=task.host.password,
    insecure=True) as client:

    response = client.subscribe(subscribe=subscribe1)
    for response1 in response:
        print(telemetryParser(response1))

nr.run(task=subscribe_with_pygnmi)
