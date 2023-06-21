class Bee:
    def __init__(self, type, job):
        self._type = type
        self._job = job

    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, type):
        self.type = type

    @type.deleter
    def type(self):
        del self.type

    @property
    def job(self):
        return self._job

