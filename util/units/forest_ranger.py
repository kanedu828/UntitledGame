from unit import Unit, Faction, AttackType

class ForestRanger(Unit):

    NAME = 'Forest Ranger'

    FACTIONS = [Faction.WILD]

    ATTACK_TYPE = AttackType.RANGED

    BASE_STATS = {
        'hp': 25,
        'attack': 18,
        'magic': 0,
        'armor': 1,
        'resistance': 3,
        'speed': 12,
        'crit_chance': 5,
        'cooldown': 2,
        'dodge': 0
    }

    def __init__(self):
        super().__init__(self.NAME, self.FACTIONS, self.ATTACK_TYPE, self.BASE_STATS)

    def passive(self, friendly_team, opposing_team, target):
        return

    def ability(self, friendly_team, opposing_team, target):
        game_log = f"{friendly_team['name']}\'s {self.name} used Snipe! "
        game_log += self.attack(friendly_team, opposing_team, target, friendly_bonus={'crit_chance': 10}, opposing_bonus={'dodge': -100})
        return game_log

    def level_growth(self, stats):
        pass

    def star_growth(self, stats):
        pass
