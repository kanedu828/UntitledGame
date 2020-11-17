from util.unit import Unit, Faction, AttackType
import random

class Gin(Unit):

    NAME = 'Gin'

    FACTIONS = [Faction.PHANTOM]

    ATTACK_TYPE = AttackType.RANGED

    BASE_STATS = {
        'hp': 20,
        'attack': 30,
        'magic': 0,
        'armor': 2,
        'resistance': 2,
        'speed': 5,
        'crit_chance': 100,
        'cooldown': 1,
        'dodge': 0
    }

    def __init__(self):
        super().__init__(self.NAME, self.FACTIONS, self.ATTACK_TYPE, self.BASE_STATS)
        self.passive_description = 'Gin loads his gun and cannot attack.'
        self.ability_description = 'Gin fires a shot.'

    def action(self, friendly_team, opposing_team):
        game_log = ''
        unit_position = friendly_team['team'].index(self)
        target_position = self.get_target(unit_position, friendly_team, opposing_team)
        if self.ability_charge >= self.stats['cooldown']:
            self.ability_charge = 0
            game_log += self.ability(friendly_team, opposing_team, target_position)
        else:
            self.ability_charge += 1
            game_log += f"{friendly_team['name']}\'s Gin is loading his gun."
        if opposing_team['team'][target_position].current_hp <= 0:
            game_log += f"\n{opposing_team['name']}\'s {opposing_team['team'][target_position].name} has been defeated."
        return game_log

    def passive(self, friendly_team, opposing_team, target):
        return

    def ability(self, friendly_team, opposing_team, target):
        unit_position = friendly_team['team'].index(self)
        #Retrieve the opposing unit to be targeted
        target_position = self.get_target(unit_position, friendly_team, opposing_team)
        return self.attack(friendly_team, opposing_team, target_position)

    def level_growth(self, levels):
        pass

    def star_growth(self, stars):
        pass
