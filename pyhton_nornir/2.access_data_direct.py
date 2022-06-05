from nornir import InitNornir

nr = InitNornir(config_file="config.yaml")
print(nr.inventory.hosts)
for group in nr.inventory.groups:
  print(nr.inventory.groups[group].data['ntp_server'])
for host in nr.inventory.hosts:
  print(nr.inventory.hosts[host].data['ntp_server'])
