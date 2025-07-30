from pyats import aetest

class TestcaseOne(aetest.Testcase):

    @aetest.setup
    def setup(self):
        # Access the testbed passed from Robot Framework
        testbed = self.parent.parameters['testbed']
        self.r1 = testbed.devices['R1']

        # We assume the device is already connected by Robot Framework
        # No need to call self.r1.connect()

        # Run a command and parse its output
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

if __name__ == '__main__':
    aetest.main()
