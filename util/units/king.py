from unit import Unit, Faction, AttackType

class King(Unit):

    NAME = 'King'

    FACTIONS = [Faction.NOBLE, Faction.CHAMPION]

    ATTACK_TYPE = AttackType.CLOSE

    BASE_STATS = {
        'hp': 80,
        'attack': 10,
        'magic': 0,
        'armor': 7,
        'resistance': 2,
        'speed': 6,
        'crit_chance': 0,
        'cooldown': 3,
        'dodge': 0
    }

    def __init__(self):
        super().__init__(self.NAME, self.FACTIONS, self.ATTACK_TYPE, self.BASE_STATS)

    def passive(self, friendly_team, opposing_team, target):
        return

    def ability(self, friendly_team, opposing_team, target):
        for unit in friendly_team['team']:
            if not unit == None:
                new_stats = unit.stats.copy()
                new_stats['armor'] += 5
                unit.set_stats(new_stats)
        return f"{friendly_team['name']}\'s {self.name} buffed his entire team by 5 armor."

    def level_growth(self, stats):
        pass

    def star_growth(self, stats):
        pass
