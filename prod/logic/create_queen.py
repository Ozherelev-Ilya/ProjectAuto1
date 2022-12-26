import const
from random import randint
from random import choice
from prod.model.queen import *


queen_bee = Queen(choice(const.NameQueen), choice(const.TypeBee),
                  randint(const.ProductionQueen[0], const.ProductionQueen[1]))

# a = queen_bee
# print(a.name, a.type, a.production)
