from nornir import InitNornir
from nornir_scrapli.tasks import netconf_get_config
#from nornir_netconf.plugins.tasks import netconf_get_config
from nornir_utils.plugins.functions import print_result

nr = InitNornir(config_file="config.yaml")

filter1 = """
  <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
  </interfaces>
"""

filter2 = """
    <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
      <router>
      </router>
    </native>
"""

filter3 = """
    <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
      <router>
        <router-ospf xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-ospf">
        </router-ospf>
      </router>
    </native>
"""

filter4 = """
    <network-instances xmlns="http://openconfig.net/yang/network-instance">
      <network-instance>
        <protocols>
          <protocol>
            <bgp>
            </bgp>
          </protocol>
        </protocols>
      </network-instance>
    </network-instances>
"""

filter5 = """
    <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
      <router>
        <bgp xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-bgp">
        </bgp>
      </router>
    </native>
"""


def netconf_subtree_get_config(task):
    task.run(task=netconf_get_config, source="running", filter_type="subtree", filter_=filter3)
#    task.run(task=netconf_get_config, source="running", xmldict="false", filter_type="subtree", path=filter3)

results = nr.run(task=netconf_subtree_get_config)
print_result(results)
