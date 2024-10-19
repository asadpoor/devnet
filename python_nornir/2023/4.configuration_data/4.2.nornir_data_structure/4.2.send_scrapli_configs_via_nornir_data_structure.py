from nornir import InitNornir
from nornir_scrapli.tasks import send_configs
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

def send_scrapli_configs_via_nornir_data_structure_example(task):
    task.run(task=send_configs, configs=[\
    f"router eigrp {task.host['hosts_data']['eigrp']['as']}", \
    f"snmp-server community {task.host['router_data']['snmp']['community']}", \
    f"ntp server {task.host['all_data']['ntp']['server']}" \
    ])

nr.run(task=load_data)
results = nr.run(task=send_scrapli_configs_via_nornir_data_structure_example)
print_result(results)
