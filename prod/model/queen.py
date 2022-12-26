from prod.model.bee import Bee


class Queen(Bee):
    def __init__(self, name, type, production):
        super().__init__(name, type)
        self._production = production

    @property
    def name(self):
        return self._name

    @property
    def type(self):
        return self._type

    @property
    def production(self):
        return self._production


