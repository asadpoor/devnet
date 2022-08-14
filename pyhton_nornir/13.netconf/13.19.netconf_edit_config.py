from nornir import InitNornir
from nornir_scrapli.tasks import netconf_edit_config
#from nornir_netconf.plugins.tasks import netconf_edit_config
from nornir_utils.plugins.functions import print_result
from nornir_jinja2.plugins.tasks import template_file

nr = InitNornir(config_file="config.yaml")

def netconf_edit_config_example(task):
    template1 = task.run(task=template_file, template="ospf_config.j2", path="./")
    ospf_config = template1.result
    task.run(task=netconf_edit_config, target="candidate", config=ospf_config)

results = nr.run(task=netconf_edit_config_example)
print_result(results)
