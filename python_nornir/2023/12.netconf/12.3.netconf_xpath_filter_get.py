from nornir import InitNornir
from nornir_scrapli.tasks import netconf_get
#from nornir_netconf.plugins.tasks import netconf_get
from nornir_utils.plugins.functions import print_result

nr = InitNornir(config_file="config.yaml")

def netconf_xpath_get(task):
#    task.run(task=netconf_get, filter_type="xpath", filter_="//in-octets")
    task.run(task=netconf_get, filter_type="xpath", filter_="/interfaces/interface/statistics/in-octets")

#    task.run(task=netconf_get, xmldict="false", filter_type="xpath", path="//in-octets")
#    task.run(task=netconf_get, xmldict="false", filter_type="xpath", path="/interfaces/interface/statistics/in-octets")

results = nr.run(task=netconf_xpath_get)
print_result(results)
