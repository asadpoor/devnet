#!/usr/bin/env python


from ncclient import manager
import xmltodict
import xml.dom.minidom



# Create an XML configuration template for ietf-interfaces
xml_config = """
<config>
                <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
                        <router>
                                <router-ospf xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-ospf">
                                        <ospf>
                                                <process-id>
                                                        <id>1</id>
                                                        <network>
                                                                <ip>192.168.1.0</ip>
                                                                <wildcard>0.0.0.255</wildcard>
                                                                <area>0</area>
                                                        </network>
                                                        <network>
                                                                <ip>192.168.2.0</ip>
                                                                <wildcard>0.0.0.255</wildcard>
                                                                <area>0</area>
                                                        </network>
                                                        <network>
                                                                <ip>192.168.3.0</ip>
                                                                <wildcard>0.0.0.255</wildcard>
                                                                <area>1</area>
                                                        </network>
                                                        <router-id>1.1.1.1</router-id>
                                                </process-id>
                                        </ospf>
                                </router-ospf>
                        </router>
                </native>
</config>"""



# Open a connection to the network device using ncclient
with manager.connect(
        host = "192.168.1.95",
        port="830",
        username="rayka",
        password="rayka",
        hostkey_verify=False
        ) as m:

    print("Sending a <edit-config> operation to the device.\n")
    # Make a NETCONF <get-config> query using the filter
    netconf_reply = m.edit_config(xml_config, target = 'running')

print("Here is the raw XML data returned from the device.\n")
# Print out the raw XML that returned
print(xml.dom.minidom.parseString(netconf_reply.xml).toprettyxml())
print("")
