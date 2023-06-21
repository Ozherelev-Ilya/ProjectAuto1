class Bee_Worker:
    def __init__(self, type, job, efficiency):
        super().__init__(type, job)
        self._efficiency = efficiency

    @property
    def efficiency(self):
        return self._efficiency

    @efficiency.setter
    def efficiency(self, efficiency):
        self._efficiency = efficiency

    @efficiency.deleter
    def efficiency(self):
        del self._efficiency

