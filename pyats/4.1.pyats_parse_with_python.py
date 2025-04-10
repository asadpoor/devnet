import json
from genie.testbed import load

# Load the testbed file
testbed = load("testbed.yaml")

# Get all devices from the testbed
devices = testbed.devices

# Iterate over each device and parse any supported commands
for device_name, device in devices.items():
    print(f"Connecting to {device_name}...")
    # Connect to the device
    device.connect(log_stdout=False)

    # Parse any supported commands
    #parsed_output = device.parse("show ip interface brief")
    #parsed_output = device.parse("show version")
    parsed_output = device.parse("show ip route")
    #parsed_output = device.parse("show ip ospf neighbor")

    parsed_output_json = json.dumps(parsed_output,indent=2)

    # Print the parsed output
    print(f"Parsed output for {device_name}:")
    print(parsed_output_json)


    try:
        routes = parsed_output["vrf"]["default"]["address_family"]["ipv4"]["routes"]

        print(f"\nRoutes Lists for {device_name}:")
        for route, details in routes.items():
            print(f"- Route: {route}")
    except KeyError:
        print("Error: Some expected keys are missing in the parsed output.")


    print("\n")

    # Disconnect from the device
    device.disconnect()
