from prod.model.bee import Bee


class Worker(Bee):
    def __init__(self, name, type, job):
        super().__init__(name, type)
        self._job = job

    @property
    def name(self):
        return self._name

    @property
    def type(self):
        return self._type

    @property
    def job(self):
        return self._job


