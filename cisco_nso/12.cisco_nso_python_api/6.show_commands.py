import ncs

with ncs.maapi.single_read_trans("admin", "python") as t:
    root = ncs.maagic.get_root(t)
    device_object = root.devices.device["R1"]

    input1 = device_object.live_status.ios_stats__exec.show.get_input()
    #input1.args = ["ip interface brief"]
    input1.args = ["cdp neighbor detail"]
    output = device_object.live_status.ios_stats__exec.show(input1).result
    print(output)
