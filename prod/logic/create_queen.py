import const
from random import choice
from prod.model.queen import Queen


queen_bee = Queen(choice(const.NameQueen), choice(const.TypeBee))

a = queen_bee
print(a.name, a.type, a.job)
