from prod.model.bee_worker import Bee_Worker
from prod.model.queen import Queen
from prod.model.drone import Drone
from prod.model.bee import Bee
import const
from random import choice

class Beehive:
    def __init__(self):
        self._population = []

    def add(self, bee):
        if isinstance(bee, Bee):
            self._population.append(bee)

    def __len__(self):
        return len(self._population)

    def 



# a = Beehive()
# w = Drone(type = choice(const.TypeBee),  eating = 2)
# a.add(w)
# print(len(a))
