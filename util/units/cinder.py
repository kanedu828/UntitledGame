from util.unit import Unit, Faction, AttackType, Status

class Cinder(Unit):

    NAME = 'Cinder'

    FACTIONS = [Faction.INFERNAL]

    ATTACK_TYPE = AttackType.CLOSE

    BASE_STATS = {
        'hp': 65,
        'attack': 5,
        'magic': 0,
        'armor': 7,
        'resistance': 7,
        'speed': 6,
        'crit_chance': 0,
        'cooldown': 2,
        'dodge': 0
    }

    def __init__(self):
        super().__init__(self.NAME, self.FACTIONS, self.ATTACK_TYPE, self.BASE_STATS)
        self.ability_description = 'Backline units gain +3 attack/speed'

    def passive(self, friendly_team, opposing_team, target):
        return

    def ability(self, friendly_team, opposing_team, target):
        game_log = f"{friendly_team['name']}\'s {self.name} used Overdrive! Teammates behind him are more powerful."
        if not friendly_team['team'][3] == None:
            three_new_stats = friendly_team['team'][3].stats.copy()
            three_new_stats['attack'] += 3
            three_new_stats['speed'] += 3
            friendly_team['team'][3].set_stats(three_new_stats)
        if not friendly_team['team'][2] == None:
            two_new_stats = friendly_team['team'][2].stats.copy()
            two_new_stats['attack'] += 3
            two_new_stats['speed'] += 3
            friendly_team['team'][2].set_stats(two_new_stats)
        return game_log


    def level_growth(self, levels):
        pass

    def star_growth(self, stars):
        pass
