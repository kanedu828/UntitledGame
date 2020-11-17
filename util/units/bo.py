from util.unit import Unit, Faction, AttackType, Status

class Bo(Unit):

    NAME = 'Bo'

    FACTIONS = [Faction.CHAMPION]

    ATTACK_TYPE = AttackType.CLOSE

    BASE_STATS = {
        'hp': 50,
        'attack': 20,
        'magic': 0,
        'armor': 5,
        'resistance': 5,
        'speed': 12,
        'crit_chance': 25,
        'cooldown': 2,
        'dodge': 25
    }

    def __init__(self):
        super().__init__(self.NAME, self.FACTIONS, self.ATTACK_TYPE, self.BASE_STATS)
        self.ability_description = 'Bo strikes twice.'

    def passive(self, friendly_team, opposing_team, target):
        pass

    def ability(self, friendly_team, opposing_team, target):
        game_log = f"{friendly_team['name']}\'s {self.name} used Double Strike! "
        self.passive(friendly_team, opposing_team, target)
        game_log += self.attack(friendly_team, opposing_team, target) + '. '
        target = self.get_target(friendly_team['team'].index(self), friendly_team, opposing_team)
        if target >= 0:
            game_log += self.attack(friendly_team, opposing_team, target)
        return game_log


    def level_growth(self, levels):
        pass

    def star_growth(self, stars):
        pass
