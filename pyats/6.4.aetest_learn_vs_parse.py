import json
from pyats import aetest
from pyats.topology import loader

testbed = loader.load('testbed.yaml')

class CommonSetup(aetest.CommonSetup):

    @aetest.subsection
    def connect_to_devices(self):
        testbed.connect()

class TestcaseOne(aetest.Testcase):
    '''
    Learning options:
    '['acl', 'arp', 'bgp', 'device', 'dot1x', 'eigrp', 'fdb', 'hsrp', 'igmp',
    'interface', 'isis', 'lag', 'lisp', 'lldp', 'management', 'mcast', 'mld',
    'msdp', 'nd', 'ntp', 'ospf', 'pim', 'platform', 'prefix_list', 'rip',
    'route_policy', 'routing', 'static_routing', 'stp', 'terminal', 'utils', 'vlan', 'vrf', 'vxlan', 'config']'
    '''
    @aetest.setup
    def setup(self):
        self.r1 = testbed.devices['R1']
        self.parsed_interface = self.r1.learn("interface")
        self.parsed_interface_json=self.parsed_interface.info

    @aetest.test
    def test1(self):
        print(json.dumps(self.parsed_interface_json, indent=4, sort_keys=True))

class CommonCleanup(aetest.CommonCleanup):

    @aetest.subsection
    def disconnect_from_devices(self):
        testbed.disconnect()

if __name__ == '__main__':
    aetest.main()
