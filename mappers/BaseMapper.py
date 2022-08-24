from abc import ABC

class BaseMapper(ABC):
	
	def __init__(self, npc):
		self.npc = npc

	def parse(self):
		attr_list = ['name', 'size', 'alignment', 'type', 'subtype', 'source', 'armor_class', 'hit_points', 'hit_dice', 'proficiency', 'challenge_rating', 'strength', 'dexterity', 'constitution', 'intelligence', 'wisdom', 'charisma', 'walk_speed', 'senses', 'languages', 'saving_throws', 'skills', 'skills_expertise', 'damage_resistances', 'damage_vulnerability', 'damage_immunities', 'condition_immunities', 'caster_spell_slots', 'actions', 'special_abilities', 'legendary_actions', 'reactions']
		parsed_npc = dict()
		for attr in attr_list:
			func = getattr(self, attr)
			parsed_npc[attr] = func()
		return parsed_npc

	def calcProficiency(self, cr_float):
		if cr_float < 5:
			return 2
		if cr_float < 9:
			return 3
		if cr_float < 13:
			return 4
		if cr_float < 17:
			return 5
		if cr_float < 21:
			return 6
		if cr_float < 25:
			return 7
		if cr_float < 29:
			return 8
		return 9

	def name(self):
		raise NotImplementedError

	def size(self):
		raise NotImplementedError

	def alignment(self):
		return "Unaligned"

	def type(self):
		return ""

	def subtype(self):
		return ""

	def source(self):
		return ""

	def armor_class(self):
		raise NotImplementedError

	def hit_points(self):
		raise NotImplementedError

	def hit_dice(self):
		return ""

	def proficiency(self):
		raise NotImplementedError

	def challenge_rating(self):
		raise NotImplementedError

	def strength(self):
		raise NotImplementedError

	def dexterity(self):
		raise NotImplementedError

	def constitution(self):
		raise NotImplementedError

	def intelligence(self):
		raise NotImplementedError

	def wisdom(self):
		raise NotImplementedError

	def charisma(self):
		raise NotImplementedError

	def walk_speed(self):
		return ""

	def senses(self):
		return {}

	def languages(self):
		raise NotImplementedError

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
		raise NotImplementedError

	def special_abilities(self):
		return []

	def legendary_actions(self):
		return []

	def reactions(self):
		return []
