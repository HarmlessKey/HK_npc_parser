from email.iterators import typed_subpart_iterator
import re

from .BaseMapper import BaseMapper

class FiveEMapper(BaseMapper):
	
	def name(self):
		return self.npc['name']

	def size(self):
		baseSize = self.npc['size'][0]
		sizeTable = {
			'T': 'Tiny',
			'S': 'Small',
			'M': 'Medium',
			'L': 'Large',
			'H': 'Huge',
			'G': 'Gargantuan',
		}

		return sizeTable[baseSize]

	def type(self):
		type_wrap = self.npc["type"]
		if type(type_wrap) == str:
			return type_wrap.capitalize()
		if type(type_wrap) == dict:
			return str(type_wrap.get('type', "")).capitalize()
		else:
			print(type(type_wrap), hasattr(type_wrap, 'type'))
		return ""

	def subtype(self):
		if type(self.npc['type']) == dict:
			return ", ".join(map(str.capitalize, self.npc["type"].get('tags', [])))
		return ""

	def source(self):
		source = f"{self.npc['source']} {self.npc['page']}"
		# source += f" [{', '.join(map(lambda s: s['source'], self.npc['otherSources']))}]"
		return source

	def armor_class(self):
		# Atm only account for base AC, not buffed AC such as mage armor
		baseAC = self.npc['ac'][0]
		if type(baseAC) == dict:
			baseAC = baseAC['ac']
		
		return int(baseAC)
			

	def hit_points(self):
		return self.npc['hp'].get('average', 1)
		
	def hit_dice(self):
		return str(self.npc['hp'].get('formula', '1d1')).split(' ')[0]

	def proficiency(self):
		return self.calcProficiency(self.challenge_rating())

	def challenge_rating(self):
		from fractions import Fraction
		cr = self.npc.get('cr', 0)
		if type(cr) == dict:
			cr = cr.get('cr', 0)
		return float(Fraction(cr))

	def strength(self):
		return self.npc['str']

	def dexterity(self):
		return self.npc['dex']

	def constitution(self):
		return self.npc['con']

	def intelligence(self):
		return self.npc['int']

	def wisdom(self):
		return self.npc['wis']

	def charisma(self):
		return self.npc['cha']

	def walk_speed(self):
		speed = self.npc.get('speed', {}).get('walk', 0)
		if type(speed) == dict:
			speed = speed.get('number', 0)
		return int(speed)
	
	def swim_speed(self):
		return int(self.npc.get('speed', {}).get('swim', 0))

	def fly_speed(self):
		return int(self.npc.get('speed', {}).get('fly', 0))

	def burrow_speed(self):
		return int(self.npc.get('speed', {}).get('burrow', 0))

	def climb_speed(self):
		return int(self.npc.get('speed', {}).get('climb', 0))

	def senses(self):
		return {}

	def languages(self):
		return self.npc.get('languages', [])

	def saving_throws(self):
		return []

	def skills(self):
		return []

	def skills_expertise(self):
		return []

	def damage_resistances(self):
		return []

	def damage_vulnerability(self):
		return []

	def damage_immunities(self):
		return []

	def condition_immunities(self):
		return []

	def caster_spell_slots(self):
		return []

	def actions(self):
		return self.parseActions(self.npc.get('action', []))

	def special_abilities(self):
		return self.parseActions(self.npc.get('trait', []))

	def legendary_actions(self):
		return self.parseActions(self.npc.get('legendary', []), True)
		
	def reactions(self):
		return self.parseActions(self.npc.get('reaction', []))

	def parseActions(self, src_actions, legendary=False):
		actions = list()

		leg_cost_regex = r"\(Costs (\d+) Actions\)"
		attack_type_regex = r"\{\@atk\s(.+?)\}"
		to_hit_regex = r"\{\@hit\s(\d+?)\}"
		damage_roll_regex = r"\{\@damage\s(?P<N>\d+)d(?P<D>\d+)\s[+-]\s(?P<M>\d+)?\}"
		dmg_types = ["acid", "bludgeoning", "cold", "fire", "force", "lightning", "necrotic", "piercing", "poison", "psychic", "radiant", "slashing", "thunder"]
		attack_type_lut = {
			'mw': "melee_weapon",
			'rw': "ranged_weapon",
			'ms': "spell_attack",
			'rs': "spell_attack"
		}

		for src_action in src_actions:
			name = src_action['name']
			action = {
				"action_list": [
					{
						"rolls": [],
					}
				],
				"desc": "",
				"name": name
			}

			if legendary:
				leg_cost_match = re.search(leg_cost_regex, name)
				leg_cost = leg_cost_match.group(1) if leg_cost_match else 1
				action['legendary_cost'] = int(leg_cost)

			for entry in src_action['entries']:
				if type(entry) == dict:
					# entry contains an ordered list
					if entry['type'] == 'list':
						for item in entry['items']:
							combined_item = f"{item['name']}. {item['entry']}"
							action['desc'] += "\n" + combined_item
						continue
						
				attack_type_match = re.search(attack_type_regex, entry)
				if attack_type_match:
					# Use this in future to create split melee and ranged weapon attack now just take first option
					attack_type = attack_type_match.group(1).split(',')[0]
					action['action_list'][0]['type'] = attack_type_lut[attack_type]
				else:
					action['action_list'][0]['type'] = "other"

				to_hit_match = re.search(to_hit_regex, entry)
				if to_hit_match:
					to_hit = to_hit_match.group(1)
					action['action_list'][0]['attack_bonus'] = int(to_hit)

				damage_roll_match = re.search(damage_roll_regex, entry)
				if damage_roll_match:
					N, D, M = damage_roll_match.groups()
					damage_type = [t for t in dmg_types if t in entry][0] if damage_roll_match else None
					
					roll = {
						"damage_type": damage_type,
						"dice_count": int(N),
						"dice_type": int(D),
						"fixed_val": int(M),
						"miss_mod": 0
					}
					action['action_list'][0]['rolls'].append(roll)

				action['desc'] = entry

			actions.append(action)
		return actions