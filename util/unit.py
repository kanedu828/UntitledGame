from abc import ABC, abstractmethod
import random

class Faction:
    NOBLE = 'noble'
    INFERNAL = 'infernal'
    PHANTOM = 'phantom'
    WILD = 'wild'
    CHAMPION = 'champion'

    FACTION_BONUS = {
        'noble': {
            2: {'armor': 3},
            4: {'armor': 10},
        },
        'infernal': {
            2: {'attack': 3},
            4: {'attack': 8, 'speed': 3},
        },
        'phantom': {
            2: {'magic': 3},
            4: {'magic': 5, 'resistance': 5},
        },
        'wild': {
            2: {'resistance': 3},
            4: {'resistance': 5, 'dodge': 10},
        },
        'champion': {
            2: {'hp': 20},
            4: {'hp': 40, 'cooldown': -1}
        }
    }

class AttackType:
    CLOSE = 'close'
    RANGED = 'ranged'
    MIXED = 'mixed'

    RANGED_PRIORITY = {
        0: [2,3,0,1],
        1: [3,2,1,0],
        2: [0,1,2,3],
        3: [1,0,3,2],
    }

    CLOSE_PRIORITY = {
        0: [0,1,2,3],
        1: [1,0,3,2],
        2: [0,1,2,3],
        3: [1,0,3,2],
    }

class Status:
    NONE = 'none'
    STUNNED = 'stunned'


class Unit(ABC):
    """
    An abstract class that represents a unit in the game. Every unit should extend this class.
    Extending classes should contain the following static variables:
    NAME : Unit's name

    FACTION : Unit's faction

    ATTACK_TYPE : Unit's attack type

    BASE_STATS : Dictionary of the unit's stats

    Attributes
    ----------
    name : str
        The name of the unit.
    faction : str
        The faction that the unit belongs to.
    level : int
        The level of the unit. Ranges from 1 to 20.
    stars : int
        The stars of a unit. Stars are obtained by merging duplicate units. Ranges from 0 to 5.
    potential : int
        The potential of a unit. Ranges from 0 to 3.
    stats : dict
        Contains int values for all the combat stats in a unit.
        hp : int
            Amount of health the unit has.
        attack : int
            The amount of attack power the unit has.
        magic : int
            The amount of magic power the unit has.
        armor : int
            The amount of armour the unit has. Protects against attack damage.
        resistance : int
            The amout of resistance the unit has. Protects against magic damage.
        speed : int
            The amount of speed the unit has. The higher speed it has, the unit will have more turns.
        crit_chance : int
            The critical chance the unit has. Ranges from 0 to 100. Calculated as a percentage as crit_chacne / 100.
        cooldown : int
            Determines how often the unit's ability will trigger.
        dodge : int
            The dodge chance the unit has. Ranges from 0 to 100. Calculated as a percentage as dodge / 100.


    Average Stats:
        HP: 50
        ATK: 15
        MGC: 15
        ARMOR: 5
        RESISTANCE:5
        SPEED: 10 1/speed
        CRIT: 0

        Average: 85

        --------------------------
        CD
        DODGE

    """
    def __init__(self, name: str, factions: str, attack_type: str, stats):
        self.name = name
        self.factions = factions
        self.attack_type = attack_type
        self.set_stats(stats)
        self.current_hp = stats['hp']
        self.ability_charge = 0
        self.status = Status.NONE

    def get_target(self, unit_position, friendly_team, opposing_team) -> int:
        if self.attack_type == AttackType.CLOSE:
            if ((unit_position == 2 or unit_position == 3)
                and ((not opposing_team['team'][0] == None and friendly_team['team'][0].current_hp > 0) or (not opposing_team['team'][1] == None and friendly_team['team'][1].current_hp > 0))):
                return -1
            else:
                for position in AttackType.CLOSE_PRIORITY[unit_position]:
                    if not opposing_team['team'][position] == None and opposing_team['team'][position].current_hp > 0:
                        target_position = position
                        break

        elif self.attack_type == AttackType.RANGED:
            for position in AttackType.RANGED_PRIORITY[unit_position]:
                if not opposing_team['team'][position] == None and opposing_team['team'][position].current_hp > 0:
                    target_position = position
                    break
        return target_position

    def get_effective_stats(self, bonus):
        effective_stats = self.stats.copy()
        for stat, value in bonus.items():
            effective_stats[stat] += value
        return effective_stats

    def attack(self, friendly_team, opposing_team, target, friendly_bonus={}, opposing_bonus={}):
        game_log = ''
        effective_stats = self.get_effective_stats(friendly_bonus)
        opposing_effective_stats = opposing_team['team'][target].get_effective_stats(opposing_bonus)
        damage = max(effective_stats['attack'] - opposing_effective_stats['armor'], 0) + max(effective_stats['magic'] - opposing_effective_stats['resistance'], 0)
        if random.randint(1,100) <= effective_stats['crit_chance']:
            damage *= 2
        if random.randint(1,100) <= opposing_effective_stats['dodge']:
            game_log += f"{opposing_team['name']}\'s {opposing_team['team'][target].name} has dodged {friendly_team['name']}\'s {self.name}\'s attack"
        else:
            opposing_team['team'][target].current_hp -= damage
            game_log += f"{friendly_team['name']}\'s {self.name} dealt {damage} damage to {opposing_team['name']}\'s {opposing_team['team'][target].name}"
        if opposing_team['team'][target].current_hp <= 0:
            game_log += f"\n{opposing_team['name']}\'s {opposing_team['team'][target].name} has been defeated."
        return game_log

    def action(self, friendly_team, opposing_team):
        """
            Attacks an opposing unit and activates the unit's passive

            Parameters
            ----------
            friendly_team : list
                List of the units on the same team
            opposing_team : list
                List of units on the opposing team

            Returns
            -------
            String of the log of what happened.
        """
        if self.status == Status.STUNNED:
            self.status = Status.NONE
            return f"{friendly_team['name']}\'s {self.name} is stunned!"
        game_log = ''
        unit_position = friendly_team['team'].index(self)
        #Retrieve the opposing unit to be targeted
        target_position = self.get_target(unit_position, friendly_team, opposing_team)
        if target_position < 0:
            self.ability_charge += 1
            return f"{friendly_team['name']}\'s {self.name} is not in range to attack."
        #Trigger ability if unit ability charge count = unit cooldown.
        if self.ability_charge >= self.stats['cooldown']:
            self.ability_charge = 0
            game_log = self.ability(friendly_team, opposing_team, target_position)
        else:
            game_log = self.attack(friendly_team, opposing_team, target_position)
            self.passive(friendly_team, opposing_team, target_position)
            self.ability_charge += 1
        self.status = Status.NONE
        if opposing_team['team'][target_position].current_hp <= 0:
            game_log += f"\n{opposing_team['name']}\'s {opposing_team['team'][target_position].name} has been defeated."
        return game_log

    def get_rating(self) -> int:
        """
            Returns the total of a unit's major statistical categories. Rough estimation of
            a unit's value.

            Returns
            -------
            int
                Sum of the unit's HP, attack, magic, armor, resistance, and speed
        """
        return stats['hp'] + stats['attack'] + stats['magic'] + int((stats['attack'] + stats['magic']) * 1 / stats['crit_chance']) + stats['armor'] + stats['resistance'] + stats['speed'];

    def set_stats(self, stats):
        """
            Sets the stats to the stats specified in the Parameters

            Raises
            ------
            AttributeError if the stats are not valid stats.

            Parameters
            ----------
            stats : dict
                Dictionary of combat stats
        """
        stats_list = ['hp', 'attack', 'magic', 'armor', 'resistance', 'speed', 'crit_chance', 'cooldown', 'dodge']
        for stat in stats_list:
            if stat not in stats:
                raise AttributeError
            #No stat should be negative.
            if stats[stat] < 0:
                stats[stat] = 0
        if stats['hp'] <= 0:
            raise AttributeError
        if stats['crit_chance'] > 100:
            stats['crit_chacne'] = 100
        if stats['dodge'] > 100:
            stats['dodge'] = 100
        self.stats = stats

    @abstractmethod
    def passive(self, friendly_team, opposing_team, target):
        """
            A unit's passive triggers every turn.

            Parameters
            ----------
            game_state : object
                The game state that the passive manipulates
        """
        pass

    @abstractmethod
    def ability(self, friendly_team, opposing_team, target):
        """
            A unit's ability triggers every self.cooldown turns

            Parameters
            ----------
            game_state : object
                The game state that the passive manipulates
        """
        pass

    @abstractmethod
    def level_growth(self, stats):
        """
            A unit's stat growth based on their level.
        """
        pass

    @abstractmethod
    def star_growth(self, stats):
        """
            A unit's stat growth based on their stars.
        """
        pass
