from nornir import InitNornir
from nornir_scrapli.tasks import send_config
from nornir_utils.plugins.functions import print_result

nr = InitNornir(config_file="config.yaml")

def access_data(task):
    print(task.host['community'])

result = nr.run(task=access_data)
print_result(result)