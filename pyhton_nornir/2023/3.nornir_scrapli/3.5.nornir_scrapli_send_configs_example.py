from nornir import InitNornir
from nornir_scrapli.tasks import send_configs
from nornir_utils.plugins.functions import print_result

nr = InitNornir(config_file="config.yaml")

def nornir_scrapli_send_configs_example(task):
    task.run(task=send_configs, configs=["router ospf 1" , "router-id 11.11.11.11" , "network 192.168.1.11 0.0.0.0 area 0"])

results = nr.run(task=nornir_scrapli_send_configs_example)
print_result(results)

