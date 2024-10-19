from nornir import InitNornir
from nornir_scrapli.tasks import send_command
from nornir_utils.plugins.functions import print_result

nr = InitNornir(config_file="config.yaml")

results = nr.run(task=send_command, command="show version | inc XE")
print_result(results)
