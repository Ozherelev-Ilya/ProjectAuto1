from prod.model.bee import Bee


class Queen(Bee):
    def __init__(self, name, type, job = "Queen"):
        super().__init__(type, job)
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @name.deleter
    def name(self):
        del self._name



    # @property
    # def type(self):
    #     return self._type
    #
    # @property
    # def job(self):
    #     return self._job

