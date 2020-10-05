from unit import Unit, Faction, AttackType

class Executioner(Unit):

    NAME = 'Executioner'

    FACTIONS = [Faction.INFERNAL]

    ATTACK_TYPE = AttackType.CLOSE

    BASE_STATS = {
        'hp': 50,
        'attack': 15,
        'magic': 0,
        'armor': 4,
        'resistance': 2,
        'speed': 9,
        'crit_chance': 5,
        'cooldown': 2,
        'dodge': 0
    }

    def __init__(self):
        super().__init__(self.NAME, self.FACTIONS, self.ATTACK_TYPE, self.BASE_STATS)

    def passive(self, friendly_team, opposing_team, target):
        return

    def ability(self, friendly_team, opposing_team, target):
        game_log = f"{friendly_team['name']}\'s {self.name} used Execute! "
        if opposing_team['team'][target].current_hp <= self.stats['attack']:
            opposing_team['team'][target].current_hp = 0
            game_log += 'Execute was successful.'
        else:
            game_log += self.attack(friendly_team, opposing_team, target)
        return game_log

    def level_growth(self, stats):
        pass

    def star_growth(self, stats):
        pass
