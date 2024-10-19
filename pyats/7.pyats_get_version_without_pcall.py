import time
from pyats.topology.loader import load

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
    devices = testbed.devices

    # Connect to each device one by one and get version
    for device_name, device in devices.items():
        get_version(device=device)

    # Record the end time
    end_time = time.time()

    # Print the time taken for the execution
    print(f"Execution time (sequential): {end_time - start_time} seconds")

if __name__ == "__main__":
    main()
