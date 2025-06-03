from pyats import aetest
from pyats.topology import loader

testbed = loader.load('testbed.yaml')

class common_setup(aetest.CommonSetup):
    """Common Setup Section"""
    
    @aetest.subsection
    def connect_to_devices(self):
        testbed.connect(log_stdout=False)

    @aetest.subsection
    def loop_mark(self):
        aetest.loop.mark(MyTestcase, device_name=testbed.devices.keys())

class MyTestcase(aetest.Testcase):
    
    @aetest.test
    def setup(self, device_name):
        self.device = testbed.devices[device_name]

    @aetest.test
    def make_change(self):
        self.device.configure('''
            interface loopback100
            description "This is a new loopback interface"
            ip address 10.10.100.100 255.255.255.0
            no shut
        ''')

class common_cleanup(aetest.CommonCleanup):
    """Common Cleanup Section"""
    
    @aetest.subsection
    def disconnect_from_devices(self):
        testbed.disconnect()

if __name__ == '__main__':
    # Run the test
    aetest.main()
