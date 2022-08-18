from nornir import InitNornir
from nornir_netconf.plugins.tasks import netconf_edit_config
from nornir_utils.plugins.functions import print_result

nr = InitNornir(config_file="config.yaml")

config1 = """
    <configuration>
            <interfaces>
                <interface>
                    <name>ge-0/0/1</name>
                    <unit>
                        <name>0</name>
                        <family>
                            <inet>
                                <address>
                                    <name>192.168.10.250/24</name>
                                </address>
                            </inet>
                        </family>
                    </unit>
                </interface>
            </interfaces>
    </configuration>
"""

def netconf_edit_config_juniper(task):
    task.run(task=netconf_edit_config, target="candidate", config=config1)

nr_filter = nr.filter(platform="junos")
results = nr_filter.run(task=netconf_edit_config_juniper)
print_result(results)
