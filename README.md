# HK_npc_parser
Tool that allows NPCs exported from [5e.tools](https://5e.tools) to be mapped to the schema that is importable in [Harmless Key](https://harmlesskey.com).

This tool is only meant for people that own the published work in which exported/imported NPCs are released. We do not condone [piracy](https://harmlesskey.com/compendium/monsters/bandit).

### Prerequisites
install python: https://www.python.org/downloads/
### Usage
1. Go to https://5e.tools and select from bestiary which npcs you want, and export.

2. Store 5e.tools npc dump (list of monsters) in `source_npcs`.
	- 5e.tools can export multiple monsters in one bundle
3. Run `python parse5etools.py`   
4. Parsed npcs stored in `hk_npcs`
	- Npcs will be each stored separately
	- Npcs will be stored in a bundle file based on input bundle
5. Import those npcs in bulk in https://HarmlessKey.com, or separately


### To Do
1. Save type actions
2. Recharge / Limited use
3. Versatile actions
4. Defences
5. Spellcasting
6. Skills
7. Saving Throws
8. Senses
9. Alignment
10. Reach
11. AOE type