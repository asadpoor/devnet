import ncs

with ncs.maapi.single_read_trans("admin", "python") as t:
    root = ncs.maagic.get_root(t)
    for box in root.devices.device:
      print("devicename:", box.name)
      print("device model:", box.platform.model)
      print("device address:", root.devices.device[box.name].address)
      print("device authentication group:", root.devices.device[box.name].authgroup)
      print("!!!!!!!!!!!!!!!!!!!!!!!!!")
