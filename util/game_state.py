from util.unit import Faction

class GameState():
    """
        Attributes
        ----------
        team_one : dict
            Dictionary containing the name and team of the users

    """
    def __init__(self, team_one, team_two):
        self.team_one = team_one
        self.team_two = team_two

    def is_alive(self, team):
        for unit in team:
            if not unit == None and unit.current_hp > 0:
                return True
        return False

    def apply_faction_bonus(self, team):
        faction_frequency = {}
        for unit in team:
            if unit:
                for faction in unit.factions:
                    if faction not in faction_frequency:
                        faction_frequency[faction] = 1
                    else:
                        faction_frequency[faction] += 1
        for unit in team:
            if unit:
                for faction in unit.factions:
                    new_stats = unit.stats.copy()
                    if faction_frequency[faction] >= 4:
                        new_stats = unit.get_effective_stats(Faction.FACTION_BONUS[faction][4])
                    elif faction_frequency[faction] >= 2:
                        new_stats = unit.get_effective_stats(Faction.FACTION_BONUS[faction][2])
                    unit.set_stats(new_stats)

    def run_game(self):
        game_log = ''
        self.apply_faction_bonus(self.team_one['team'])
        self.apply_faction_bonus(self.team_two['team'])
        team_one_priority = [(unit, 1 / unit.stats['speed'], 1 / unit.stats['speed'], 1) for unit in self.team_one['team'] if not unit == None]
        team_two_priority = [(unit, 1 / unit.stats['speed'], 1 / unit.stats['speed'], 2) for unit in self.team_two['team'] if not unit == None]
        sorted_units = sorted(team_one_priority + team_two_priority, key=lambda a : 1 / a[0].stats['speed'])
        priority = []
        speed_increment = sorted_units[0][1]
        current_time = speed_increment
        lowest_frequency = sorted_units[len(sorted_units) - 1][1]

        while current_time <= lowest_frequency:
            priority += [(unit, team) for unit, frequency, current_frequency, team in sorted_units if current_frequency <= current_time]
            for i in range(len(sorted_units)):
                if sorted_units[i][2] <= current_time:
                    sorted_units[i] = (sorted_units[i][0], sorted_units[i][1], sorted_units[i][2] + sorted_units[i][1], sorted_units[i][3])
            sorted_units = sorted(sorted_units, key=lambda a : a[2])
            current_time += speed_increment
            if current_time > lowest_frequency:
                priority += [(unit, team) for unit, frequency, current_frequency, team in sorted_units if current_frequency <= lowest_frequency]

        while self.is_alive(self.team_one['team']) and self.is_alive(self.team_two['team']):
            for unit, team in priority:
                if unit.current_hp > 0:
                    if team == 1:
                        game_log += '\n' + unit.action(self.team_one, self.team_two)
                    else:
                        game_log += '\n' + unit.action(self.team_two, self.team_one)
                if not (self.is_alive(self.team_one['team']) and self.is_alive(self.team_two['team'])):
                    break
        if self.is_alive(self.team_one['team']):
            game_log += '\n' + 'Team 1 wins!'
        else:
            game_log += '\n' + 'Team 2 wins!'
        return game_log
