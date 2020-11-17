from util.unit import Unit, Faction, AttackType, Status

class Onna(Unit):

    NAME = 'Onna'

    FACTIONS = [Faction.NOBLE]

    ATTACK_TYPE = AttackType.RANGED

    BASE_STATS = {
        'hp': 30,
        'attack': 0,
        'magic': 7,
        'armor': 4,
        'resistance': 4,
        'speed': 10,
        'crit_chance': 0,
        'cooldown': 2,
        'dodge': 0
    }

    FRIENDLY_TARGET = None

    def __init__(self):
        super().__init__(self.NAME, self.FACTIONS, self.ATTACK_TYPE, self.BASE_STATS)
        self.passive_description = 'Onna follows the nearest teammate. Additionally, Onna grants 3 attack to whoever she follows.'
        self.ability_description = 'Onna grants her followed teammate 2 ability charges.'

    def get_friendly_target(self, friendly_team):
        unit_index = friendly_team['team'].index(self)
        priority = {
            0: [1, 2, 3],
            1: [0, 3, 2],
            2: [3, 0, 1],
            3: [2, 1, 0],
        }
        for position in priority[unit_index]:
            if not friendly_team['team'][position] == None and friendly_team['team'][position].current_hp > 0:
                return position
        return -1

    def passive(self, friendly_team, opposing_team, target):
        if self.FRIENDLY_TARGET == None or self.FRIENDLY_TARGET.current_hp <= 0:
            friendly_target = self.get_friendly_target(friendly_team)
            if friendly_target < 0:
                self.FRIENDLY_TARGET = None
            else:
                self.FRIENDLY_TARGET = friendly_team['team'][friendly_target]
                new_stats = self.FRIENDLY_TARGET.stats.copy()
                new_stats['attack'] += 3
                self.FRIENDLY_TARGET.set_stats(new_stats)

    def ability(self, friendly_team, opposing_team, target):
        game_log = f"{friendly_team['name']}\'s {self.name} used Cheer! "
        self.passive(friendly_team, opposing_team, target)
        if not self.FRIENDLY_TARGET == None:
            self.FRIENDLY_TARGET.ability_charge += 2
        return game_log


    def level_growth(self, levels):
        pass

    def star_growth(self, stars):
        pass
