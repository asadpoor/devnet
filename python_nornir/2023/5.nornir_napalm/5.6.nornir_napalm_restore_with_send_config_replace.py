from nornir import InitNornir
from nornir_napalm.plugins.tasks import napalm_configure
from nornir_utils.plugins.functions import print_result

nr = InitNornir(config_file="config.yaml")

def nornir_napalm_restore_with_send_config_replace(task):
    task.run(task=napalm_configure, filename=f"{task.host}", replace=True)

results=nr.run(task=nornir_napalm_restore_with_send_config_replace)
print_result(results)
