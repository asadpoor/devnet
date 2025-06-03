import json
from genie.testbed import load
from pyats.async_ import pcall
from pyats import aetest
from genie.conf import Genie

class PingCheck(aetest.Testcase):
    @aetest.setup
    def setup(self, testbed):
        self.testbed = load(testbed)
        self.device_list = [dev for dev in self.testbed.devices.values()]

    @aetest.test
    def check_ping(self):
        def ping_test(device):
            device.connect(log_stdout=False)
            output = device.execute("ping 8.8.8.8")
            print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
            print("device=",device.name," ping output=",output)
            print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
            device.disconnect()

        pcall(ping_test, device=self.device_list)


if __name__ == '__main__':
    aetest.main()
