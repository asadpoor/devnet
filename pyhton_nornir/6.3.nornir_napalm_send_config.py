from dataclasses import replace
from nornir import InitNornir
from nornir_napalm.plugins.tasks import napalm_configure
from nornir_utils.plugins.functions import print_result

nr = InitNornir(config_file="config.yaml")

def napalm_send_config_exmaple(task):
    task.run(task=napalm_configure, filename="config_list")

results=nr.run(task=napalm_send_config_exmaple)
print_result(results)
