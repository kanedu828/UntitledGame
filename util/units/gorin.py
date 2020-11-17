from util.unit import Unit, Faction, AttackType, Status

class Gorin(Unit):

    NAME = 'Gorin'

    FACTIONS = [Faction.PHANTOM]

    ATTACK_TYPE = AttackType.RANGED

    BASE_STATS = {
        'hp': 63,
        'attack': 8,
        'magic': 2,
        'armor': 5,
        'resistance': 8,
        'speed': 8,
        'crit_chance': 0,
        'cooldown': 2,
        'dodge': 0
    }

    UNCOLLECTED_SOULS = [0,1,2,3]

    def __init__(self):
        super().__init__(self.NAME, self.FACTIONS, self.ATTACK_TYPE, self.BASE_STATS)
        self.passive_description = 'Whenever an opposing unit dies, gain +2 armour and resistance.'
        self.ability_description = 'Gorin pulls his target to the frontline.'

    def passive(self, friendly_team, opposing_team, target):
        """
            Whenever an opposing unit dies, gain +2 armour and resistance.
        """
        stat_buffs = 0
        for position in self.UNCOLLECTED_SOULS:
            if position > 0 and not opposing_team['team'][position] == None and opposing_team['team'][position].current_hp <= 0:
                stat_buffs += 2
                position -= 4
        stat_bonus = {
            'armor': stat_buffs,
            'resistance': stat_buffs,
        }
        self.set_stats(self.get_effective_stats(stat_bonus))

    def ability(self, friendly_team, opposing_team, target):
        game_log = f"{friendly_team['name']}\'s {self.name} used Hook! {opposing_team['team'][target].name} was pulled to the front-line!."
        pull_position = max(target - 2, target)
        target_unit = opposing_team['team'][target]
        opposing_team['team'][target] = opposing_team['team'][pull_position]
        opposing_team['team'][pull_position] = target_unit
        return game_log


    def level_growth(self, levels):
        pass

    def star_growth(self, stars):
        pass
