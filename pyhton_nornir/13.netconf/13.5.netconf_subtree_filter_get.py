from nornir import InitNornir
from nornir_scrapli.tasks import netconf_get
#from nornir_netconf.plugins.tasks import netconf_get
from nornir_utils.plugins.functions import print_result

nr = InitNornir(config_file="config.yaml")

filter1 = """
  <interfaces xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper">
  </interfaces>
"""

filter2 = """
  <interfaces xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper">
    <interface>
      <statistics>
      </statistics>
    </interface>
  </interfaces>
"""

filter3 = """
  <interfaces xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper">
    <interface>
      <statistics>
          <in-octets>
          </in-octets>
      </statistics>
    </interface>
  </interfaces>
"""

filter4 = """
  <interfaces xmlns="http://openconfig.net/yang/interfaces">
      <interface>
        <state>
          <name>
          </name>
          <counters>
            <in-octets>
            </in-octets
          </counters>
        </state>
      </interface>
  </interfaces>
"""

def netconf_subtree_get(task):
    task.run(task=netconf_get, filter_type="subtree", filter_=filter4)
#    task.run(task=netconf_get, xmldict="false", filter_type="subtree", path=filter4)

results = nr.run(task=netconf_subtree_get)
print_result(results)
