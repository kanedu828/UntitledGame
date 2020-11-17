from util.unit import Unit, Faction, AttackType
import random

class Tor(Unit):

    NAME = 'Tor'

    FACTIONS = [Faction.NOBLE]

    ATTACK_TYPE = AttackType.CLOSE

    BASE_STATS = {
        'hp': 50,
        'attack': 10,
        'magic': 0,
        'armor': 5,
        'resistance': 2,
        'speed': 8,
        'crit_chance': 0,
        'cooldown': 2,
        'dodge': 0
    }

    def __init__(self):
        super().__init__(self.NAME, self.FACTIONS, self.ATTACK_TYPE, self.BASE_STATS)
        self.ability_description = 'Tor attacks and gains 2 armour.'

    def passive(self, friendly_team, opposing_team, target):
        return

    def ability(self, friendly_team, opposing_team, target):
        game_log = f"{friendly_team['name']}\'s {self.name} used Protective Blow! "
        game_log += self.attack(friendly_team, opposing_team, target)
        new_stats = self.stats.copy()
        new_stats['armor'] += 2
        self.set_stats(new_stats)
        return game_log

    def level_growth(self, levels):
        pass

    def star_growth(self, stars):
        pass
