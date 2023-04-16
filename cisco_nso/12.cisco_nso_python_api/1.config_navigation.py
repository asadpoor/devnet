import ncs

with ncs.maapi.single_read_trans("admin", "python") as t:
    root = ncs.maagic.get_root(t)
    device_object = root.devices.device["R1"]
    #print(dir(device_object))
    # instead of dir you can xpath command in nso to find the path

    #print(dir(device_object.platform))
    #print(device_object.platform.model)

    #print(dir(device_object.config))
    #print(dir(device_object.config.ios__interface))
    #print(dir(device_object.config.ios__interface.GigabitEthernet))
    # show running-config devices device R1 config interface | display xpath
    #print(device_object.config.ios__interface.GigabitEthernet[1].ip.address.primary.address)
    for interface in device_object.config.ios__interface.GigabitEthernet:
      int_name = interface.name
      int_ip = interface.ip.address.primary.address
      int_mask = interface.ip.address.primary.mask
      print("Interface GigabitEthernet {} has an IP address of {} and a mask of {}".format(int_name, int_ip, int_mask))
