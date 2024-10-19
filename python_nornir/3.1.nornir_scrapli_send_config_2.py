from nornir import InitNornir
from nornir_scrapli.tasks import send_config
from nornir_utils.plugins.functions import print_result

nr = InitNornir(config_file="config.yaml")

def snmp_config(task):
    task.run(task=send_config, config=f"snmp-server community {task.host['community']}")

results = nr.run(task=snmp_config)
print_result(results)

