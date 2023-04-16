import ncs
with ncs.maapi.single_write_trans('admin', 'python') as t:
    root = ncs.maagic.get_root(t)
    device_object = root.devices.device["R1"].config

    # enable cdp
    device_object.ios__cdp.run = True

    # add loopback interface
    device_object.ios__interface["Loopback"].create("1337")
    device_object.ios__interface.Loopback["1337"].ip.address.primary.address = "192.168.1.1"
    device_object.ios__interface.Loopback["1337"].ip.address.primary.mask = "255.255.255.252" 

    # commit the configuration
    t.apply()
