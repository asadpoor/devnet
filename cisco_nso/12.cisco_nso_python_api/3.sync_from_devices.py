import ncs
with ncs.maapi.single_read_trans('admin', 'python') as t:
    root = ncs.maagic.get_root(t)
    devices  = root.devices
    device_object  = root.devices.device["R1"]
    result = device_object.sync_from()
