from pyats import aetest
from pyats.topology import loader

testbed = loader.load('testbed.yaml')

class CommonSetup(aetest.CommonSetup):
    @aetest.subsection
    def load_testbed(self):
        devices = [device for device in testbed.devices]
        aetest.loop.mark(DeviceTest, device=devices)

class DeviceTest(aetest.Testcase):
    @aetest.test
    def test_device(self, device):
        device = testbed.devices[device]
        device.connect(log_stdout=False)
        print(f"{device} interfaces ...",device.parse("show ip interface brief"))
        device.disconnect()

if __name__ == '__main__':
    aetest.main()
