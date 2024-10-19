from nornir import InitNornir
from nornir_scrapli.tasks import send_commands_from_file
from nornir_utils.plugins.functions import print_result

nr = InitNornir(config_file="config.yaml")

results = nr.run(task=send_commands_from_file, file="command_list")
print_result(results)
