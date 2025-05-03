from pyats import aetest
from pyats.topology import loader

# Load the testbed
testbed = loader.load('testbed.yaml')

class MyCommonSetup(aetest.CommonSetup):
    @aetest.subsection
    def connect_to_devices(self):
        testbed.connect(log_stdout=False)

class MyTestcase(aetest.Testcase):
    @aetest.setup
    def setup(self):
        # Initialize dictionary to store L3 interfaces
        self.l3_interfaces = {}
        # Filter devices by OS in setup
        for device_name, device in testbed.devices.items():
            if getattr(device, 'os', None) == 'iosxe':
                self.l3_interfaces[device_name] = device
            else:
                print(f"Skipping {device_name} because OS is {getattr(device, 'os', 'unknown')}")

    @aetest.test
    def test_l3_interfaces(self):
        # Process L3 interfaces for filtered devices
        for device_name, device in self.l3_interfaces.items():
            interfaces = device.parse("show ip interface brief")
            print(f"Results for {device_name}:")
            print(interfaces)

class CommonCleanup(aetest.CommonCleanup):
    @aetest.subsection
    def disconnect_from_devices(self):
        testbed.disconnect()

if __name__ == '__main__':
    aetest.main(testbed=testbed)
