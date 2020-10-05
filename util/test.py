from units.temple_guard import TempleGuard
from units.executioner import Executioner
from units.ghost_mage import GhostMage
from units.forest_ranger import ForestRanger
from units.rajon import Rajon
from units.gin import Gin
from units.forsn import Forsn
from units.king import King
from units.cinder import Cinder
from game_state import GameState
import copy

temple_guard = TempleGuard()
executioner = Executioner()
forest_ranger = ForestRanger()
ghost_mage = GhostMage()
rajon = Rajon()
gin = Gin()
forsn = Forsn()
king = King()
cinder = Cinder()

team_one = [copy.copy(king), None, copy.copy(forest_ranger), copy.copy(forest_ranger)]

team_two = [copy.copy(seth), copy.copy(seth), copy.copy(forest_ranger), copy.copy(forest_ranger)]

game = GameState({'name': 'Team 1', 'team': team_one}, {'name': 'Team 2', 'team': team_two})

print(game.run_game())
