
__name__ = "__tools__"


class VerletIntegration:
    """This generates the Verlet integration up to some time.
    Solution to the newtonic equations of motion"""
    def __init__(self, limit, acceleration):
        self.limit = limit
        self.a = acceleration
        self.dt = 0.1
        self.verlet_terms = []

    def __contains__(self, item):
        for x in VerletIntegration(self.limit):
            self.verlet_terms.append(x)
        return item in self.verlet_terms

    def __iter__(self):
        self.x, self.v = 0, 0
        self.time = 0
        while self.time <= self.limit:
            yield self.x
            self.x = self.x + self.v * self.dt + 0.5 * self.a * (self.dt**2)


if __name__ == "__main__":
    for i in VerletIntegration(500, 10):
        print(i)
