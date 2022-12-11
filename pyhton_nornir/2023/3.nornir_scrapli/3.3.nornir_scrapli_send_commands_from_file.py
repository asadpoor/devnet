from nornir import InitNornir
from nornir_scrapli.tasks import send_commands_from_file
from nornir_utils.plugins.functions import print_result

nr = InitNornir(config_file="config.yaml")

def nornir_scrapli_send_commands_from_file_example(task):
    task.run(task=send_commands_from_file, file="command_list.txt")

results = nr.run(task=nornir_scrapli_send_commands_from_file_example)
print_result(results)
