from genie.testbed import load

testbed = load("testbed.yaml")
devices = testbed.devices
R1 = testbed.devices["R1"]
R1.connect(log_stdout=False)

bgp_state = R1.learn("bgp")

R1.disconnect()

# Print BGP feature output
print("BGP state structured output: \n", bgp_state.info)

# Extract and print the list of neighbors
neighbors = bgp_state.info['instance']['default']['vrf']['default']['neighbor']
print("\nList of BGP Neighbors: ")
for neighbor_ip, neighbor_info in neighbors.items():
    print(f"Neighbor IP: {neighbor_ip}")
    print(f"Remote AS: {neighbor_info['remote_as']}")
    print(f"Session State: {neighbor_info['session_state']}")
    print("-" * 50)
