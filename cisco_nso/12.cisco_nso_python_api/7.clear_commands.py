import ncs

with ncs.maapi.single_read_trans("admin", "python") as t:
    root = ncs.maagic.get_root(t)
    device_object = root.devices.device["R1"]

    input1 = device_object.live_status.ios_stats__exec.clear.get_input()
    input1.args = ["cdp counters"]
    output = device_object.live_status.ios_stats__exec.clear(input1).result
    print(output)
