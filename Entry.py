# Basis Measure class to implement one 'Entry' in the Evidence list.

class Entry:
    def __init__(self, values, prob):
        self.focalset = values
        self.confidence = prob

    def get_focalset(self):
        return self.focalset

    def get_confidence(self):
        return self.confidence

    def set_focalset(self, values):
        self.focalset = values

    def set_confidence(self, prob):
        self.confidence = prob
