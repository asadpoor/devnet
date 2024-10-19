import time
from pyats.topology.loader import load
from pyats.async_ import pcall

def get_version(device):
    # Connect to device
    device.connect()
    # Parse "show version" output
    sh_ver = device.parse("show version")
    # Disconnect from device
    device.disconnect()
    # Print and return output
    print(f"Parsed output for {device}:")
    print(sh_ver,"\n\n")
    return sh_ver

def main():
    # Record the start time
    start_time = time.time()

    # Load testbed
    testbed = load("testbed.yaml")

    # List of all device objects from testbed
    tb_devices = testbed.devices.values()

    # Connect and get version of each tested device in parallel
    version_results = pcall(get_version, device=tb_devices)

    # Record the end time
    end_time = time.time()

    # Print time taken for execution
    print(f"Execution time (parallel): {end_time - start_time} seconds")

if __name__ == "__main__":
    main()
