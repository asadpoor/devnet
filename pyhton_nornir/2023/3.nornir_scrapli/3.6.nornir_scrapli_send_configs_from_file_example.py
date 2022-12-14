from nornir import InitNornir
from nornir_scrapli.tasks import send_configs_from_file
from nornir_utils.plugins.functions import print_result

nr = InitNornir(config_file="config.yaml")

def nornir_scrapli_send_configs_from_file_example(task):
    task.run(task=send_configs_from_file, file="config_file.txt")

results = nr.run(task=nornir_scrapli_send_configs_from_file_example)
print_result(results)

