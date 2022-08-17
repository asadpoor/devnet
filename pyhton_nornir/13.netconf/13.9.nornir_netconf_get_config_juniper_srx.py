from nornir import InitNornir
from nornir_netconf.plugins.tasks import netconf_get_config

nr = InitNornir(config_file="config.yaml")

filter1 = """
    <configuration>
    </configuration>
"""

filter2 = """
    <configuration>
      <system>
        <login>
          <user>
          </user>
        </login>
      </system>
    </configuration>
"""

filter3 = """
    <configuration>
      <interfaces>
        <interface>
        </interface>
      </interfaces>
    </configuration>
"""

filter4 = """
    <configuration>
      <routing-options>
        <static>
          <route>
          </route>
        </static>
      </routing-options>
    </configuration>
"""

def netconf(task):
#    config = task.run(task=netconf_get_config, source="running", xmldict="false")
    config = task.run(task=netconf_get_config, source="running", xmldict="false", filter_type="subtree", path=filter4)
    config = config.result
    config = config["rpc"]
    print(config)
#    for key, value in config.items():
#      print("key=",key)
#      print("value=",value)

nr_filter = nr.filter(platform="junos")
results=nr_filter.run(task=netconf)
