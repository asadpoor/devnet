from nornir import InitNornir
from nornir_scrapli.tasks import send_config
from nornir_utils.plugins.functions import print_result

nr = InitNornir(config_file="config.yaml")

def nornir_scrapli_send_config_example(task):
    task.run(task=send_config, config="snmp-server community rayka-co.com RO")

results = nr.run(task=nornir_scrapli_send_config_example)
print_result(results)

