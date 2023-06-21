import const
from random import randint
from random import choice
from prod.model.beehive import Beehive
from prod.model.queen import Queen

# count_queen = 1
# count_bee = randint(const.quantity_bee[0], const.quantity_bee[1])
# count_drone = int(count_nectariferous * 0.02)



queen_bee = Queen(choice(const.NameQueen), choice(const.TypeBee))

# a = Beehive
# a.add(queen_bee)
# print(a)

print(queen_bee.name, queen_bee.type, queen_bee.job)

