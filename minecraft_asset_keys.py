"""
Outputs a file of all the keys used in Minecraft's blocks and items
"""

import json
import pathlib
import os
import pprint
from enum import Enum, unique, auto

@unique
class Asset(Enum):
    def _generate_next_value_(name, start, count, last_values):
        return name.lower()

    BLOCK = auto()
    ITEM = auto()

home = str(pathlib.Path.home())
path = f"{home}/.minecraft/resourcepacks/pack/assets/minecraft/models"

output_name = "data"
output_path = f"{home}/Documents/{output_name}"

for asset_type in list(Asset):
	# print(asset_type.value)
	
	_, _, names = next(os.walk(f"{path}/{asset_type.value}"))

	# print(names)

	keys = {}

	for i in names:
		with open(f"{path}/{asset_type.value}/{i}") as f:
		    c = json.load(f)
		    # print(c, "-----")
		    for k, v in c.items():
		        if k in keys:
		            if isinstance(v, dict):
		                keys[k].update(v)
		            elif isinstance(v, str):
		                keys[k] = v
		            else:
		                keys[k] = keys[k] + v
		        else:
		            keys[k] = v

	# print(keys)
	# print(json.dumps(keys, indent=4, sort_keys=True))
	pprint.pprint(keys)

	with open(f"{output_path}-{asset_type.value}.json", 'w') as f:
		json.dump(keys, f, ensure_ascii=False, indent=4)

print("Finished!")

