from BasisMeasure import BasisMeasure

class DempsterRule:
    def __init__(self, bm1, bm2):
        self.bm1 = bm1
        self.bm2 = bm2
        self.bmout = BasisMeasure(None, None)

        for x in self.bm1.getentries():
            for y in self.bm2.getentries():

        # bmout.addentry