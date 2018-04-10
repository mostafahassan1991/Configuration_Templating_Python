# this code to generate configuration templates for cisco switches by the use of jinja2 and yaml python libraries
# and then we will push these configuration to devices by the use of netmiko python library

from jinja2 import Environment, FileSystemLoader
import yaml
import os


with open("Devices_meta_data", 'r') as stream:
    Devices = (yaml.load(stream))

THIS_DIR = os.path.dirname(os.path.abspath(__file__))
print THIS_DIR
j2_env = Environment(loader=FileSystemLoader(THIS_DIR), trim_blocks=True)


for device, data in Devices.iteritems():
    configuration = j2_env.get_template('template').render(data)
    with open(os.path.join(THIS_DIR, device + ".txt"), 'w') as y:
        y.write(configuration)
