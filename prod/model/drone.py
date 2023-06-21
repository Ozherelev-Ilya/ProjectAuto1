from prod.model.bee import Bee
import const
from random import choice

class Drone(Bee):
    def __init__(self, type, eating, job = "drone"):
        super().__init__(type, job)
        self._eating = eating

    @property
    def eating(self):
        return self._eating

    @eating.setter
    def eating(self, eating):
        self._eating = eating

    @eating.deleter
    def eating(self):
        del self._eating


# a=Drone
# print(a)