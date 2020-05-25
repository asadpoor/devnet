#!/usr/bin/env python


from ncclient import manager
import xmltodict
import xml.dom.minidom
from yaml import safe_load
from jinja2 import Environment, FileSystemLoader
import credential

hosts = ["192.168.1.95", "192.168.1.95"]

with open(f"data.yml", "r") as handle:
    ospf_data = safe_load(handle)

j2_env = Environment (loader=FileSystemLoader("."), trim_blocks=True, autoescape=True)
template = j2_env.get_template(f"ospf_config.j2")
ospf_config = template.render(data=ospf_data["ospf"])

for host in hosts:
    # Open a connection to the network device using ncclient
    with manager.connect(
            host = hosts[0],
            port = 830,
            username = credential.IOS_XE["username"],
            password = credential.IOS_XE["password"],
            hostkey_verify=False
            ) as m:

        print("Sending a <edit-config> operation to the device.\n")
        # Make a NETCONF <get-config> query using the filter
        netconf_reply = m.edit_config(ospf_config, target = 'running')

    print("Here is the raw XML data returned from the device.\n")
    # Print out the raw XML that returned
    print(xml.dom.minidom.parseString(netconf_reply.xml).toprettyxml())
    print("")
