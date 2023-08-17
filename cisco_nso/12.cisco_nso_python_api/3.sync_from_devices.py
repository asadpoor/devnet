import ncs
with ncs.maapi.single_read_trans('admin', 'python') as t:
    root = ncs.maagic.get_root(t)
    device_object  = root.devices.device["R1"]
    #print(dir(device_object))
    result = device_object.sync_from()
