from util.unit import Unit, Faction, AttackType, Status

class Willow(Unit):

    NAME = 'Willow'

    FACTIONS = [Faction.WILD]

    ATTACK_TYPE = AttackType.CLOSE

    BASE_STATS = {
        'hp': 50,
        'attack': 0,
        'magic': 5,
        'armor': 7,
        'resistance': 7,
        'speed': 10,
        'crit_chance': 0,
        'cooldown': 3,
        'dodge': 0
    }

    def __init__(self):
        super().__init__(self.NAME, self.FACTIONS, self.ATTACK_TYPE, self.BASE_STATS)
        self.ability_description = 'Willow heals his teammates for 7 health.'

    def passive(self, friendly_team, opposing_team, target):
        pass

    def ability(self, friendly_team, opposing_team, target):
        game_log = f"{friendly_team['name']}\'s {self.name} used Herbal Heal! "
        for unit in friendly_team['team']:
            if not unit == None and unit.current_hp > 0:
                unit.current_hp += 7
        return game_log


    def level_growth(self, levels):
        pass

    def star_growth(self, stars):
        pass
