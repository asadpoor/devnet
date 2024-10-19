from nornir import InitNornir
from nornir_scrapli.tasks import netconf_get
#from nornir_netconf.plugins.tasks import netconf_get
from nornir_utils.plugins.functions import print_result

nr = InitNornir(config_file="config.yaml")

def netconf_xpath_get(task):
    task.run(task=netconf_get, filter_type="xpath", filter_="//in-octets")
#    task.run(task=netconf_get, filter_type="xpath", filter_="//v4-protocol-stats/in-octets")

#    task.run(task=netconf_get, xmldict="false", filter_type="xpath", path="//in-octets")
#    task.run(task=netconf_get, xmldict="false", filter_type="xpath", path="//v4-protocol-stats/in-octets")

results = nr.run(task=netconf_xpath_get)
print_result(results)
