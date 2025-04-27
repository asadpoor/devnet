from pyats import aetest
from pyats.topology import loader

testbed = loader.load('testbed.yaml')

class MyCommonSetup(aetest.CommonSetup):

    @aetest.subsection
    def connect_to_devices(self):
        testbed.connect(log_stdout=False)

class MyTestcase(aetest.Testcase):

    @aetest.setup
    def setup(self):
        self.devices = testbed.devices

        self.l3_interfaces = {}
        for device_name, device in self.devices.items():
            self.l3_interfaces[device_name] = device.parse("show ip interface brief")

    @aetest.test
    def test1(self):
        for device_name, interfaces in self.l3_interfaces.items():
            print(f"Results for {device_name}:")
            print(interfaces)

class CommonCleanup(aetest.CommonCleanup):
    @aetest.subsection
    def disconnect_from_devices(self):
        testbed.disconnect()

if __name__ == '__main__':
    aetest.main()
