from pyats import aetest
from pyats.topology import loader

# Load the testbed
testbed = loader.load('testbed.yaml')

class MyCommonSetup(aetest.CommonSetup):
    @aetest.subsection
    def connect_to_devices(self):
        testbed.connect(log_stdout=False)

class MyTestcase(aetest.Testcase):
    @aetest.test
    def test_l3_interfaces(self):
        l3_interfaces = {}
        for device_name, device in testbed.devices.items():
            interfaces = device.parse("show ip interface brief")
            l3_interfaces[device_name] = interfaces
            print(f"Results for {device_name}:")
            print(interfaces)

class CommonCleanup(aetest.CommonCleanup):
    @aetest.subsection
    def disconnect_from_devices(self):
        testbed.disconnect()

if __name__ == '__main__':
    aetest.main(testbed=testbed)
