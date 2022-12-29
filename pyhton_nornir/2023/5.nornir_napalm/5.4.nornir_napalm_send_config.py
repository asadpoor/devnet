from nornir import InitNornir
from nornir_napalm.plugins.tasks import napalm_configure
from nornir_utils.plugins.functions import print_result

nr = InitNornir(config_file="config.yaml")

def nornir_napalm_send_config_exmaple(task):
    #task.run(task=napalm_configure, filename="config_file_merge.txt")
    task.run(task=napalm_configure, filename="config_file_replace.txt")

results=nr.run(task=nornir_napalm_send_config_exmaple)
print_result(results)
