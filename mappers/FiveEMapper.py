
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
		return str(self.npc['type']['type']).capitalize()

	def subtype(self):
		if hasattr(self.npc['type'], 'tags'):
			return str(self.npc['type']['tags'][0]).capitalize()
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
		return int(self.npc['hp']['average'])

	def hit_dice(self):
		return str(self.npc['hp']['formula']).split(' ')[0]

	def proficiency(self):
		return self.calcProficiency(self.challenge_rating())

	def challenge_rating(self):
		from fractions import Fraction
		return float(Fraction(self.npc['cr']))

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
		if hasattr(self.npc['speed'], 'walk'):
			return int(self.npc['speed']['walk'])
		return 0

	def senses(self):
		return {}

	def languages(self):
		return self.npc['languages']

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
		return []

	def special_abilities(self):
		return []

	def legendary_actions(self):
		return []

	def reactions(self):
		return []