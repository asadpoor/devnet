from nornir import InitNornir
from nornir_scrapli.tasks import netconf_edit_config
#from nornir_netconf.plugins.tasks import netconf_edit_config
from nornir_netconf.plugins.tasks import netconf_commit
from nornir_utils.plugins.functions import print_result


#        <router-ospf xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-ospf">
#        <router-ospf operation="merge" xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-ospf">
#        <router-ospf operation="replace" xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-ospf">
#      <router operation="replace"> ;; dangerous
config1 = """
  <config>
    <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
      <router>
        <router-ospf operation="replace" xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-ospf">
          <ospf>
            <process-id>
              <id>1</id>
              <network>
                <ip>172.16.7.1</ip>
                <wildcard>0.0.0.0</wildcard>
                <area>10</area>
              </network>
              <network>
                <ip>172.17.8.1</ip>
                <wildcard>0.0.0.0</wildcard>
                <area>20</area>
              </network>
              <router-id>1.1.1.1</router-id>
            </process-id>
          </ospf>
        </router-ospf>
      </router>
    </native>
  </config>
"""



#            <bgp operation="merge">
#            <bgp operation="replace">
#            <bgp>

config2 = """
  <config>
    <network-instances xmlns="http://openconfig.net/yang/network-instance">
      <network-instance>
        <name>default</name>
        <protocols>
          <protocol>
            <identifier xmlns:oc-pol-types="http://openconfig.net/yang/policy-types">oc-pol-types:BGP</identifier>
            <name>65000</name>
            <bgp operation="replace">
              <global>
                <config>
                  <as>65000</as>
                  <router-id>2.2.2.2</router-id>
                </config>
              </global>
              <neighbors>
                <neighbor>
                  <neighbor-address>91.91.91.91</neighbor-address>
                  <config>
                    <neighbor-address>91.91.91.91</neighbor-address>
                    <peer-as>65001</peer-as>
                  </config>
                </neighbor>
                <neighbor>
                  <neighbor-address>21.21.21.21</neighbor-address>
                  <config>
                    <neighbor-address>21.21.21.21</neighbor-address>
                    <peer-as>65003</peer-as>
                  </config>
                </neighbor>
              </neighbors>
            </bgp>
          </protocol>
        </protocols>
      </network-instance>
    </network-instances>
  </config>
"""


nr = InitNornir(config_file="config.yaml")

def netconf_edit_config_example(task):
    task.run(task=netconf_edit_config, target="candidate", config=config1)
#    task.run(task=netconf_edit_config, xmldict="false", target="candidate", config=config1)
    task.run(task=netconf_commit)

results = nr.run(task=netconf_edit_config_example)
print_result(results)
