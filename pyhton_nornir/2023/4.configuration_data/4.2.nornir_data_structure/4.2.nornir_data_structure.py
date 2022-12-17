from nornir import InitNornir
from nornir_utils.plugins.functions import print_result
from nornir_utils.plugins.tasks.data import load_yaml

nr = InitNornir(config_file="config.yaml")

def load_data(task):
  hosts_data = task.run(task=load_yaml, file=f"./host_vars/{task.host}.yaml")
  router_data = task.run(task=load_yaml, file=f"./group_vars/router.yaml")
  switch_data = task.run(task=load_yaml, file=f"./group_vars/switch.yaml")
  all_data = task.run(task=load_yaml, file=f"./group_vars/all.yaml")

  task.host["hosts_data"] = hosts_data.result
  task.host["router_data"] = router_data.result
  task.host["switch_data"] = switch_data.result
  task.host["all_data"] = all_data.result


def access_nornir_hosts_data(task):
    print("###########################################")
    print("eigrp AS number of device ", task.host, " is ", task.host["hosts_data"]["eigrp"]["as"])
    for network in task.host['hosts_data']["eigrp"]["networks"]:
      print("eigrp network of device ", task.host, " is: ", network)

def access_nornir_groups_data(task):
    print("###########################################")
    print("community of router group is", task.host["router_data"]["snmp"]["community"])
    print("community of switch group is", task.host["switch_data"]["snmp"]["community"])

def access_nornir_all_data(task):
    print("###########################################")
    print("ntp server address of all devices is", task.host["all_data"]["ntp"]["server"])


results = nr.run(task=load_data)
print_result(results)

results = nr.run(task=access_nornir_hosts_data)
print_result(results)

results = nr.run(task=access_nornir_groups_data)
print_result(results)

results = nr.run(task=access_nornir_all_data)
print_result(results)

