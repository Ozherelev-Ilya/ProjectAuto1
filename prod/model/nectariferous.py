from prod.model.bee import Bee


class Nectariferous(Bee):
    def __init__(self, name, type, efficiency):
        super().__init__(name, type)
        self._efficiency = efficiency

    @property
    def name(self):
        return self._name

    @property
    def type(self):
        return self._type

    @property
    def efficiency(self):
        return self._efficiency
