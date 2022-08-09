from nornir import InitNornir
from nornir_scrapli.tasks import netconf_get_config
#from nornir_netconf.plugins.tasks import netconf_get_config
from nornir_utils.plugins.functions import print_result

nr = InitNornir(config_file="config.yaml")

def get_config(task):
#    task.run(task=netconf_get_config, filter_type="xpath", filter_="/native")
#    task.run(task=netconf_get_config, filter_type="xpath", filter_="/native/router")
#    task.run(task=netconf_get_config, filter_type="xpath", filter_="/native/router/router-ospf")
#    task.run(task=netconf_get_config, filter_type="xpath", filter_="//router-ospf")
#    task.run(task=netconf_get_config, filter_type="xpath", filter_="/native//ospf")
#    task.run(task=netconf_get_config, filter_type="xpath", filter_="//interfaces")
#    task.run(task=netconf_get_config, filter_type="xpath", filter_="/native//interface")
    task.run(task=netconf_get_config, filter_type="xpath", filter_="//bgp")


#    task.run(task=netconf_get_config, source="running", xmldict="false", filter_type="xpath", path="/native")
#    task.run(task=netconf_get_config, source="running", xmldict="false", filter_type="xpath", path="/native/router/router-ospf")
#    task.run(task=netconf_get_config, source="running", xmldict="false", filter_type="xpath", path="//router-ospf")

results = nr.run(task=get_config)
print_result(results)
