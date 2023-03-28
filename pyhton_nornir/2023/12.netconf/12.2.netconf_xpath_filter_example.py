from nornir import InitNornir
from nornir_scrapli.tasks import netconf_get_config
#from nornir_netconf.plugins.tasks import netconf_get_config
from nornir_utils.plugins.functions import print_result

nr = InitNornir(config_file="config.yaml")

def netconf_xpath_filter_example(task):
#    task.run(task=netconf_get_config, source="running")
#    task.run(task=netconf_get_config, source="running", filter_type="xpath", filter_="//address")
#    task.run(task=netconf_get_config, source="running", filter_type="xpath", filter_="//ip/address/primary/address")
#    task.run(task=netconf_get_config, source="running", filter_type="xpath", filter_="/native/interface/GigabitEthernet/ip/address")
#    task.run(task=netconf_get_config, source="running", filter_type="xpath", filter_="//wildcard")
#    task.run(task=netconf_get_config, source="running", filter_type="xpath", filter_="/native/router/router-ospf")
#    task.run(task=netconf_get_config, source="running", filter_type="xpath", filter_="//as")
#    task.run(task=netconf_get_config, source="running", filter_type="xpath", filter_="/network-instances/network-instance/protocols/protocol/bgp")
#    task.run(task=netconf_get_config, source="running", filter_type="xpath", filter_="/native")
#    task.run(task=netconf_get_config, source="running", filter_type="xpath", filter_="/native/username")
#    task.run(task=netconf_get_config, source="running", filter_type="xpath", filter_="/native/ip/access-list/standard")
#    task.run(task=netconf_get_config, source="running", filter_type="xpath", filter_="/native/router")
#    task.run(task=netconf_get_config, source="running", filter_type="xpath", filter_="/native/router/router-ospf")
#    task.run(task=netconf_get_config, source="running", filter_type="xpath", filter_="//router-ospf")
#    task.run(task=netconf_get_config, source="running", filter_type="xpath", filter_="/native//ospf")
#    task.run(task=netconf_get_config, source="running", filter_type="xpath", filter_="//interfaces")
#    task.run(task=netconf_get_config, source="running", filter_type="xpath", filter_="/native//interface")
#    task.run(task=netconf_get_config, source="running", filter_type="xpath", filter_="//bgp")
    task.run(task=netconf_get_config, source="running", filter_type="xpath", filter_="//protocol/bgp")
#    task.run(task=netconf_get_config, source="running", filter_type="xpath", filter_="/network-instances//bgp")
#    task.run(task=netconf_get_config, source="running", filter_type="xpath", filter_="//ntp")


## enable the follwoing lines with nornir_netconf plugin and disable nornir_scrapli plugin
#    task.run(task=netconf_get_config, source="running", xmldict="false")
#    task.run(task=netconf_get_config, source="running", xmldict="false", filter_type="xpath", path="/native")
#    task.run(task=netconf_get_config, source="running", xmldict="false", filter_type="xpath", path="/native/router/router-ospf")
#    task.run(task=netconf_get_config, source="running", xmldict="false", filter_type="xpath", path="//router-ospf")

results = nr.run(task=netconf_xpath_filter_example)
print_result(results)
