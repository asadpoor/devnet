from nornir import InitNornir
from nornir_scrapli.tasks import send_configs
from nornir_utils.plugins.functions import print_result

nr = InitNornir(config_file="config.yaml")

def send_configs_test(task):
    task.run(task=send_configs, configs=[f"snmp-server community {task.host['community']}", "ntp server 1.1.1.1"], dry_run="True")

results = nr.run(task=send_configs_test)
print_result(results)

