from util.unit import Unit, Faction, AttackType, Status

class Rajon(Unit):

    NAME = 'Rajon'

    FACTIONS = [Faction.WILD, Faction.CHAMPION]

    ATTACK_TYPE = AttackType.CLOSE

    BASE_STATS = {
        'hp': 55,
        'attack': 10,
        'magic': 10,
        'armor': 8,
        'resistance': 8,
        'speed': 8,
        'crit_chance': 0,
        'cooldown': 2,
        'dodge': 0
    }

    def __init__(self):
        super().__init__(self.NAME, self.FACTIONS, self.ATTACK_TYPE, self.BASE_STATS)
        self.ability_description = 'Rajon attacks and stuns the target.'

    def passive(self, friendly_team, opposing_team, target):
        return

    def ability(self, friendly_team, opposing_team, target):
        game_log = f"{friendly_team['name']}\'s {self.name} used Rooting Blow! "
        game_log += self.attack(friendly_team, opposing_team, target)
        opposing_team['team'][target].status = Status.STUNNED
        return game_log

    def level_growth(self, levels):
        pass

    def star_growth(self, stars):
        pass
