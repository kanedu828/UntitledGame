from unit import Unit, Faction, AttackType

class Forsn(Unit):

    NAME = 'Forsn'

    FACTIONS = [Faction.INFERNAL]

    ATTACK_TYPE = AttackType.CLOSE

    BASE_STATS = {
        'hp': 45,
        'attack': 20,
        'magic': 0,
        'armor': 4,
        'resistance': 2,
        'speed': 13,
        'crit_chance': 5,
        'cooldown': 2,
        'dodge': 0
    }

    def __init__(self):
        super().__init__(self.NAME, self.FACTIONS, self.ATTACK_TYPE, self.BASE_STATS)

    def passive(self, friendly_team, opposing_team, target):
        return

    def ability(self, friendly_team, opposing_team, target):
        game_log = f"{friendly_team['name']}\'s {self.name} used Blazing Blade! {self.name}\'s attack as increased. "
        new_stats = self.stats.copy()
        new_stats['attack'] += 1
        self.set_stats(new_stats)
        game_log += self.attack(friendly_team, opposing_team, target)
        return game_log

    def level_growth(self, stats):
        pass

    def star_growth(self, stats):
        pass
