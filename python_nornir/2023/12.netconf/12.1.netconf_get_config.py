from nornir import InitNornir
from nornir_scrapli.tasks import netconf_get_config
#from nornir_netconf.plugins.tasks import netconf_get_config
from nornir_utils.plugins.functions import print_result

nr = InitNornir(config_file="config.yaml")

def get_config(task):
    task.run(task=netconf_get_config, source="running")
#    task.run(task=netconf_get_config, source="running", xmldict="false")

results = nr.run(task=get_config)
print_result(results)
