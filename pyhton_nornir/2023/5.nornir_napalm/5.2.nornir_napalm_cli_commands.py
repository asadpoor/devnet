
from nornir import InitNornir
from nornir_napalm.plugins.tasks import napalm_cli
from nornir_utils.plugins.functions import print_result

nr = InitNornir(config_file="config.yaml")

def nornir_napalm_cli_commands_example(task):
    task.run(task=napalm_cli, commands=["show ip interface brief", "show version | inc XE"])

results=nr.run(task=nornir_napalm_cli_commands_example)
print_result(results)
