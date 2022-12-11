from nornir import InitNornir
from nornir_scrapli.tasks import send_config
from nornir_utils.plugins.functions import print_result

nr = InitNornir(config_file="config.yaml")
for host in nr.inventory.hosts:
  results = nr.run(task=send_config, config=f"snmp-server community {nr.inventory.hosts[host].data['community']}")
  print_result(results)

