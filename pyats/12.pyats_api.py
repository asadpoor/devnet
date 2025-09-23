from genie.testbed import load

# Load testbed
testbed = load('testbed.yaml')

# Access devices
R1 = testbed.devices['R1']
R1.connect()

routes = (R1.api.get_routes())
print("type of routes variable is ",type(routes))
print(routes)


R1.api.shut_interface(interface = 'GigabitEthernet3')

input("Press Enter to show you the result of dir(R1.api) ...")
print(dir(R1.api))
# https://developer.cisco.com/docs/genie-docs/
# then "Available APIs"


option = "interface GigabitEthernet1"
#option = ""
config_commands = R1.api.get_config_commands_from_running_config(option=option)
print(f"Configuration commands for {option}:")
print(config_commands)
