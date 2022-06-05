from nornir import InitNornir
from nornir_utils.plugins.functions import print_result

nr = InitNornir(config_file="config.yaml")
def access_data(task):
    print(task.host['community'])

results = nr.run(task=access_data)
print_result(results)

