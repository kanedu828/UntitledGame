from util.units.tor import Tor
from util.units.slade import Slade
from util.units.gho import Gho
from util.units.isla import Isla
from util.units.rajon import Rajon
from util.units.gin import Gin
from util.units.forsn import Forsn
from util.units.king import King
from util.units.cinder import Cinder
from util.units.gorin import Gorin
from util.units.bo import Bo
from util.units.willow import Willow
from util.units.onna import Onna

class Rarity:
    RARE = 'rare'
    EPIC = 'epic'
    LEGENDARY = 'legendary'

unit_list = {
    0: {
        'unit': Tor(),
        'rarity': Rarity.RARE,
    },
    1: {
        'unit': Slade(),
        'rarity': Rarity.RARE,
    },
    2: {
        'unit': Gho(),
        'rarity': Rarity.RARE,
    },
    3: {
        'unit': Isla(),
        'rarity': Rarity.RARE,
    },
    4: {
        'unit': Rajon(),
        'rarity': Rarity.LEGENDARY,
    },
    5: {
        'unit': Gin(),
        'rarity': Rarity.LEGENDARY,
    },
    6: {
        'unit': Forsn(),
        'rarity': Rarity.EPIC,
    },
    7: {
        'unit': King(),
        'rarity': Rarity.LEGENDARY,
    },
    8: {
        'unit': Cinder(),
        'rarity': Rarity.EPIC,
    },
    9: {
        'unit': Gorin(),
        'rarity': Rarity.EPIC,
    },
    10: {
        'unit': Bo(),
        'rarity': Rarity.LEGENDARY,
    },
    11: {
        'unit': Willow(),
        'rarity': Rarity.EPIC,
    },
    12: {
        'unit': Onna(),
        'rarity': Rarity.EPIC,
    },
}
