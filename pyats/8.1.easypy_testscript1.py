from pyats import aetest
from genie.testbed import load
from pyats.async_ import pcall

class Version_Check(aetest.Testcase):
    @aetest.setup
    def setup(self, testbed):
        self.testbed = load(testbed)
        self.device_list = [dev for dev in self.testbed.devices.values()]

    @aetest.test
    def check_version(self):
        def get_version(device):
            device.connect(log_stdout=False)

            output = device.parse('show version')

            print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
            print("device=",device.name," version=",output['version']['version'])
            print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

            device.disconnect()

        # Use pcall correctly by passing the devices as a positional argument
        pcall(get_version, device=self.device_list)


if __name__ == '__main__':
    aetest.main()
