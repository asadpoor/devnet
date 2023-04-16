import ncs
with ncs.maapi.single_write_trans('admin', 'python') as t:
    root = ncs.maagic.get_root(t)
    device_object = root.devices.device["R1"].config
    del device_object.ios__interface.Loopback["1337"]
    t.apply()
