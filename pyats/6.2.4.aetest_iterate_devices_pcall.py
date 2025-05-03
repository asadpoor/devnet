from pyats.aetest import Testcase, test, main
from pyats.async_ import pcall
from pyats.topology import loader

testbed = loader.load('testbed.yaml')

class MyTest(Testcase):

    @test
    def parse_interfaces(self):

        def parse_interfaces(device):
            print(f"Connecting to {device.name}...")
            device.connect(log_stdout=False)
            print(f"Parsing {device.name} interfaces...")
            parsed_output = device.parse('show ip interface brief')
            return {device.name: parsed_output}

        results = pcall(parse_interfaces, device=list(testbed.devices.values()))
        
        for result in results:
            print(result)

if __name__ == '__main__':
    main()
