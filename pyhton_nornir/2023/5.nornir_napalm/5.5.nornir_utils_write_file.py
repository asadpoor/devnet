from distutils.file_util import write_file
from nornir import InitNornir
from nornir_napalm.plugins.tasks import napalm_get
from nornir_utils.plugins.functions import print_result
from nornir_utils.plugins.tasks.files import write_file
from rich import print as rprint

nr = InitNornir(config_file="config.yaml")

def napalm_write_file_example(task):
    config=task.run(task=napalm_get, getters=["get_config"])
    running_config=config.result["get_config"]["running"]
    task.run(task=write_file, content=running_config, filename=f"{task.host}")

results=nr.run(task=napalm_write_file_example)
print_result(results)
