import json
#from genie.testbed import load
from pyats.async_ import pcall
from pyats import aetest
from genie.conf import Genie
from pyats.topology import loader

testbed = loader.load('testbed.yaml')

class VersionCheck(aetest.Testcase):
    @aetest.setup
    def setup(self):
        self.devices = [dev for dev in testbed.devices.values()]

    @aetest.test
    def check_version(self):
        os_mismatch = []

        def get_version(device):
            device.connect(log_stdout=False)
            output = device.parse('show version')
            device.disconnect()
            return output

        results = pcall(get_version, device=self.devices)

        for device, output in zip(self.devices, results):
            print("device=",device.name," version=",output['version']['version'])
            os = output['version']['os']
            if not os.startswith('IOS'):
                os_mismatch.append({
                    'device': device.name,
                    'version': os
                })

        if os_mismatch:
            self.failed(f"Devices with incorrect OS: {json.dumps(os_mismatch, indent=2)}")
        else:
            self.passed("All devices are running expected OS")

if __name__ == '__main__':
    aetest.main()
