from prod.model.bee import Bee

class Beehive:
    def __init__(self):
        self._population = []

    def add(self, population):
        if isinstance(population, Bee):
            self._population.append(self)



