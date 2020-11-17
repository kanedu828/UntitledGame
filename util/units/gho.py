from util.unit import Unit, Faction, AttackType

class Gho(Unit):

    NAME = 'Gho'

    FACTIONS = [Faction.PHANTOM]

    ATTACK_TYPE = AttackType.RANGED

    BASE_STATS = {
        'hp': 25,
        'attack': 0,
        'magic': 18,
        'armor': 0,
        'resistance': 9,
        'speed': 7,
        'crit_chance': 0,
        'cooldown': 2,
        'dodge': 0
    }

    def __init__(self):
        super().__init__(self.NAME, self.FACTIONS, self.ATTACK_TYPE, self.BASE_STATS)
        self.passive_description = 'Gho\'s target loses 1 resistance.'
        self.ability_description = 'Gho does 2 bonus magic damage.'

    def passive(self, friendly_team, opposing_team, target):
        new_stats = opposing_team['team'][target].stats.copy()
        new_stats['resistance'] -= 1
        opposing_team['team'][target].set_stats(new_stats)
        return

    def ability(self, friendly_team, opposing_team, target):
        game_log = f"{friendly_team['name']}\'s {self.name} used Haunt! "
        game_log += self.attack(friendly_team, opposing_team, target, friendly_bonus={'magic': 2})
        self.passive(friendly_team, opposing_team, target)
        return game_log

    def level_growth(self, levels):
        pass

    def star_growth(self, stars):
        pass
