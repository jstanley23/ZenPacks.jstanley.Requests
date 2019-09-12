import os
from ZenPacks.zenoss.ZenPackLib import zenpacklib


# Break out the yaml files for easy reading/editing
dirname = os.path.dirname(__file__)

# These are the main yaml files
zenpack_files = (
    'classes.yaml', # contains new devices, components and their relationships
    'device_classes.yaml', # contains new device classes and their properties
)

# Main yaml directories
yamldirs = [
    'templates', # Contains individual yamls for each template
    'eventClasses', # Contains individual yamls for each eventClass
]

yamls = [
    os.path.join(dirname, yaml_file)
    for yaml_file in zenpack_files
    if os.path.exists(os.path.join(dirname, yaml_file))
]

# Parse yaml directories for yaml files
for yamldir in yamldirs:
    yamldir = os.path.join(dirname, yamldir)
    if not os.path.exists(yamldir):
        continue
    for name in os.listdir(yamldir):
        if name.endswith('.yaml'):
            yamls.append(os.path.join(yamldir, name))

CFG = zenpacklib.load_yaml(yamls, verbose=False, level=30)
schema = CFG.zenpack_module.schema

# Patches
#from ZenPacks.jstanley.Requests import patches
