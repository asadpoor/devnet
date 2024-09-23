from pyats import aetest
from pyats.topology import loader

# Load the testbed file
testbed = loader.load('testbed.yaml')

class MyCommonSetup(aetest.CommonSetup):

    @aetest.subsection
    def connect_to_devices(self):
        testbed.connect()

class MyTestcase(aetest.Testcase):

    @aetest.setup
    def setup(self):
        self.devices = testbed.devices

        self.bgp_neighbors = {}
        for device_name, device in self.devices.items():
            self.bgp_neighbors[device_name] = device.parse("show bgp neighbors")

    @aetest.test
    def test1(self):
        for device_name, neighbors in self.bgp_neighbors.items():
            print(f"BGP neighbors of the device {device_name}:")
            print(neighbors.q.contains("Established").get_values("neighbor"))

class CommonCleanup(aetest.CommonCleanup):
    @aetest.subsection
    def disconnect_from_devices(self):
        testbed.disconnect()

if __name__ == '__main__':
    aetest.main()
