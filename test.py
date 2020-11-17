from util.unit_directory import unit_list
from util.game_state import GameState
import copy


team_one = [copy.copy(unit_list[0]['unit']), None, None, None]

team_two = [copy.copy(unit_list[1]['unit']), None, None, None]

game = GameState({'name': 'Team 1', 'team': team_one}, {'name': 'Team 2', 'team': team_two})

print(game.run_game())
