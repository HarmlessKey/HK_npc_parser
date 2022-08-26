import json
from os import path, walk
import re
from mappers.FiveEMapper import FiveEMapper

import pprint

CURR_DIR = path.dirname(path.abspath(__file__))
TARGET_NPC_DIR = path.join(CURR_DIR, 'hk_npcs')
SOURCE_NPC_DIR = path.join(CURR_DIR, 'source_npcs')

def main():
	for root, _, files in walk(SOURCE_NPC_DIR):
		for file in files:
			with open (path.join(root, file)) as input:
				npcs = json.load(input)
				new_npc_bundle = list()
				for npc in npcs:
					mapper = FiveEMapper(npc)

					new_npc = mapper.parse()
					new_npc_bundle.append(new_npc)

					new_npc_file_name = f"{new_npc['name']}_hk.json"
					new_npc_file = path.join(TARGET_NPC_DIR, new_npc_file_name)
					with open(new_npc_file, 'w') as out:
						json.dump(new_npc, out, indent=2)

				new_npc_bundle_file_name = f"{file.replace('.json', '')}_bundle_hk.json"
				new_npc_bundle_file = path.join(TARGET_NPC_DIR, new_npc_bundle_file_name)
				with open(new_npc_bundle_file, 'w') as bundle:
					json.dump(new_npc_bundle, bundle, indent=2)


def parse_float(input):
	from fractions import Fraction
	return float(Fraction(input))

if __name__ == "__main__":
	main()