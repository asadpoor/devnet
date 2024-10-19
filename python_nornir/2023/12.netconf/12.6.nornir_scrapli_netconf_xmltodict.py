from nornir import InitNornir
from nornir_scrapli.tasks import netconf_get_config
from nornir_utils.plugins.functions import print_result
import xmltodict
from pprint import pprint

nr = InitNornir(config_file="config.yaml")

filter1 = """
  <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
  </interfaces>
"""


def netconf_xmltodict(task):
    interfaces = task.run(task=netconf_get_config, source="running", filter_type="subtree", filter_=filter1)
    interfaces_dic = xmltodict.parse(interfaces.result)
    pprint(interfaces_dic)
#    pprint(interfaces_dic["rpc-reply"])
#    pprint(interfaces_dic["rpc-reply"]["data"])
#    pprint(interfaces_dic["rpc-reply"]["data"]["interfaces"])
#    pprint(interfaces_dic["rpc-reply"]["data"]["interfaces"]["interface"])
#    pprint(type(interfaces_dic["rpc-reply"]["data"]["interfaces"]["interface"]))

#    for key,value in interfaces_dic.items():
#        print("key=",key)
#        print("value=",value)

    interfaceslist = interfaces_dic["rpc-reply"]["data"]["interfaces"]["interface"]
    for interface in interfaceslist:
#        pprint(interface)
#        pprint(interface["name"])
#        pprint(interface["ipv4"])
#        pprint(interface["ipv4"]["address"])
#        pprint(interface["ipv4"]["address"]["ip"])
        print(interface["name"], " has the IP address of ", interface["ipv4"]["address"]["ip"])

results = nr.run(task=netconf_xmltodict)
