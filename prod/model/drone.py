from prod.model.bee import Bee


class Drone(Bee):
    def __init__(self, name, type, eating):
        super().__init__(name, type)
        self._eating = eating

    @property
    def name(self):
        return self._name

    @property
    def type(self):
        return self._type

    @property
    def eating(self):
        return self._eating

