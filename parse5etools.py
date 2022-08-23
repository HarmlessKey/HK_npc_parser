import json
from os import path, walk
import re


SOURCE_NPC_DIR = path.join(path.dirname(path.abspath(__file__)), 'source_npcs')
MAPPER_FILE = path.join(path.dirname(path.abspath(__file__)), 'mapper.json')
MAPPER = json.load(open(MAPPER_FILE))

def main():
	for root, dirs, files in walk(SOURCE_NPC_DIR):
		for file in files:
			with open (path.join(root, file)) as input:
				npcs = json.load(input)
				parsed = dict()
				for npc in npcs:
					for key, formula in MAPPER.items():
						new_val = formula
						attr_re = r"\{(.+?)\}"
						source_attrs = re.findall(attr_re, formula)
						for src_attr in source_attrs:
							nests = src_attr.split('.')
							target = npc
							for n in nests:
								target = target[n]

							new_val = re.sub(r"\{" + str(src_attr) + r"\}",  str(target), new_val)
						
						func_re = r"(.+?)\((.+?)\)"
						if len(re.findall(func_re, new_val)) > 0:
							match = re.search(func_re, new_val)
							func_name = match.group(1)
							func_arg = match.group(2)
							func = globals()[func_name]
							new_val = func(func_arg)
							
						print(key, new_val)

						# print(source)
						
						# parsed[key] = 



def parse_float(input):
	from fractions import Fraction
	return float(Fraction(input))

if __name__ == "__main__":
	main()