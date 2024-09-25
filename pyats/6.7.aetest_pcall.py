import json
from genie.testbed import load
from pyats.async_ import pcall
from pyats import aetest
from genie.conf import Genie

class VersionCheck(aetest.Testcase):
    @aetest.setup
    def setup(self, testbed):
        self.testbed = load(testbed)
        self.ios_xe_devices = [dev for dev in self.testbed.devices.values()]

    @aetest.test
    def check_version(self):
        version_mismatch = []

        def get_version(device):
            device.connect(log_stdout=False)
            output = device.parse('show version')
            device.disconnect()
            return output

        # Use pcall correctly by passing the devices as a positional argument
        results = pcall(get_version, device=self.ios_xe_devices)
        print("type of results = ",results)

        for device, output in zip(self.ios_xe_devices, results):
            #print("device=",device.name," ouput=",output['version']['version'])
            version = output['version']['os']
            if not version.startswith('IOS'):
                version_mismatch.append({
                    'device': device.name,
                    'version': version
                })

        if version_mismatch:
            self.failed(f"Devices with incorrect version: {json.dumps(version_mismatch, indent=2)}")
        else:
            self.passed("All devices are running expected version")

aetest.main(testbed="testbed.yaml")
