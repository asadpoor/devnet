from nornir import InitNornir
from nornir_scrapli.tasks import netconf_edit_config
#from nornir_netconf.plugins.tasks import netconf_edit_config
from nornir_netconf.plugins.tasks import netconf_commit
from nornir_utils.plugins.functions import print_result
from nornir_jinja2.plugins.tasks import template_file
from nornir_utils.plugins.tasks.data import load_yaml

# you can use one of the operations in template.
#        <router-ospf xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-ospf">
#        <router-ospf operation="merge" xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-ospf">
#        <router-ospf operation="replace" xmlns="http://cisco.co

nr = InitNornir(config_file="config.yaml")

def load_data(task):
  hosts_data = task.run(task=load_yaml, file=f"./host_vars/{task.host}.yaml")
  task.host["hdata"] = hosts_data.result


def netconf_edit_config_with_template(task):
    template_to_load = task.run(task=template_file, template="ospf.j2", path="templates")
    configuration = template_to_load.result
    task.run(task=netconf_edit_config, target="candidate", config=configuration)
#    task.run(task=netconf_edit_config, xmldict="false", target="candidate", config=configuration)
    task.run(task=netconf_commit)

nr.run(task=load_data)
results = nr.run(task=netconf_edit_config_with_template)
print_result(results)
