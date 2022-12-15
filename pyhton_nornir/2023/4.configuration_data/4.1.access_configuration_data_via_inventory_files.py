from nornir import InitNornir
from nornir_utils.plugins.functions import print_result

nr = InitNornir(config_file="config.yaml")

def access_configuration_data_via_inventory_files(task):
    print("###########################################")
    print("eigrp AS number of device ", task.host, " is ", task.host['eigrp_as'])
    for network in task.host['eigrp_networks']:
      print("eigrp network of device ", task.host, " is: ", network)

    print("community of device ", task.host, " is ", task.host['community'])

    print("ntp server address of device ", task.host, " is ", task.host['ntp_server'])

results = nr.run(task=access_configuration_data_via_inventory_files)
print("###########################################")
print_result(results)
