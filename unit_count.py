from util.unit_directory import unit_list, Rarity
from util.unit import Faction


rarities = [Rarity.RARE, Rarity.EPIC, Rarity.LEGENDARY]

factions = [Faction.NOBLE, Faction.WILD, Faction.PHANTOM, Faction.INFERNAL, Faction.CHAMPION]

for rarity in rarities:
    print(f"{rarity}: {len([key for key, value in unit_list.items() if value['rarity'] == rarity])}")

for faction in factions:
    print(f"{faction}: {len([key for key, value in unit_list.items() if faction in value['unit'].factions])}")
