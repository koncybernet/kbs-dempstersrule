class Entry:
    def __init__(self, values, prob):
        self.size = 0
        self.values = values
        self.probability = prob

    def get_values(self):
        return self.values

    def get_probability(self):
        return self.probability

    def set_values(self, values):
        self.values = values

    def set_probability(self, prob):
        self.probability = prob
