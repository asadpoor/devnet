from nornir import InitNornir
from nornir_netconf.plugins.tasks import netconf_get
from nornir_utils.plugins.functions import print_result

nr = InitNornir(config_file="config.yaml")

filter1 = """
    <rpc>
        <filter type="subtree">
        </filter>
        <get-interface-information>
                <terse/>
        </get-interface-information>
    </rpc>
"""

filter2 = """
        <get-arp-table-information>
                <interface>ge-0/0/0.0</interface>
        </get-arp-table-information>
"""

filter3 = """
<filter type="subtree">
</filter>
"""

filter4 = """
<rpc message-id="101" xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
  <get>
    <filter>
      <netconf-state xmlns="urn:ietf:params:xml:ns:yang:ietf-netconf-monitoring">
      </netconf-state>
    </filter>
  </get>
</rpc>
"""


def netconf(task):
    config = task.run(task=netconf_get, xmldict="false")
#    config = task.run(task=netconf_get, xmldict="false", filter_type="subtree", path=filter4)
    config = config.result
    config = config["rpc"]
    print(config)
#    for key, value in config.items():
#      print("key=",key)
#      print("value=",value)

nr_filter = nr.filter(platform="junos")
results=nr_filter.run(task=netconf)
print_result(results)
