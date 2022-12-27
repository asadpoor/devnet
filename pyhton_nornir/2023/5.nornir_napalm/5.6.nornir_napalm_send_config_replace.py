from dataclasses import replace
from nornir import InitNornir
from nornir_napalm.plugins.tasks import napalm_configure
from nornir_utils.plugins.functions import print_result

nr = InitNornir(config_file="config.yaml")

def nornir_napalm_send_config_exmaple(task):
    task.run(task=napalm_configure, filename=f"{task.host}", replace=True)

results=nr.run(task=nornir_napalm_send_config_exmaple)
print_result(results)
