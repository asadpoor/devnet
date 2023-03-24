from nornir import InitNornir
from nornir_netconf.plugins.tasks import netconf_get_config
from nornir_utils.plugins.functions import print_result
import xmltodict
from pprint import pprint

nr = InitNornir(config_file="config.yaml")

filter1 = """
  <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
  </interfaces>
"""


def netconf_xmltodict(task):
    interfaces = task.run(task=netconf_get_config, source="running", xmldict="true", filter_type="subtree", path=filter1)
    interfaces_dic = interfaces.result
    pprint(interfaces_dic)
#    pprint(interfaces_dic["xml_dict"])
#    pprint(interfaces_dic["xml_dict"]["data"])

    interfaceslist = interfaces_dic["xml_dict"]["data"]["interfaces"]["interface"]
#    pprint(type(interfaceslist))

#    for key,value in interfaceslist.items():
#        print("key=",key)
#        print("value=",value)

    for interface in interfaceslist:
        pprint(interface["name"])
        pprint(interface["ipv4"]["address"]["ip"])


results = nr.run(task=netconf_xmltodict)
