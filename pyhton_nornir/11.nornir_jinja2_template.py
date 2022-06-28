from nornir import InitNornir
from nornir_scrapli.tasks import send_configs
from nornir_utils.plugins.functions import print_result
from nornir_jinja2.plugins.tasks import template_file
from nornir_utils.plugins.tasks.data import load_yaml

nr = InitNornir(config_file="config.yaml")

def load_data(task):
  hosts_data = task.run(task=load_yaml, file=f"./host_vars/{task.host}.yaml")
  groups_data = task.run(task=load_yaml, file=f"./group_vars/all.yaml")
  task.host["data"] = hosts_data.result
  task.host["gdata"] = groups_data.result

def template_snmp(task):
    template = task.run(task=template_file, template=f"{task.host.platform}-ntp.j2", path="./")
    task.host["config"]=template.result
    configurations=task.host["config"].splitlines()
    task.run(task=send_configs, configs=configurations)

nr.run(task=load_data)
results = nr.run(task=template_snmp)
print_result(results)