from pyats import aetest
from pyats.topology import loader

# Load the testbed file
testbed = loader.load('testbed.yaml')

class CommonSetup(aetest.CommonSetup):

    @aetest.subsection
    def connect_to_devices(self):
        testbed.connect()

class TestcaseOne(aetest.Testcase):

    @aetest.setup
    def setup(self):
        self.r1 = testbed.devices['R1']
        self.l3_interfaces = self.r1.parse("show ip interface brief")

    @aetest.test
    def test1(self):
        print(self.l3_interfaces)

    @aetest.test
    def test2(self):
        for intf, details in self.l3_interfaces['interface'].items():
            if details['status'] == 'up':
                print(f"Interface {intf} is up.")
            else:
                print(f"Interface {intf} is not up.")

class CommonCleanup(aetest.CommonCleanup):

    @aetest.subsection
    def disconnect_from_devices(self):
        testbed.disconnect()

if __name__ == '__main__':
    aetest.main()
