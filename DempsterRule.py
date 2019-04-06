from Evidence import Evidence
from BasisMeasure import BasisMeasure

class DempsterRule:
    def __init__(self, ev1, ev2):
        self.ev1 = ev1
        self.ev2 = ev2
        self.evout = Evidence(None, None)

        for x in self.ev1.get_entries():
            for y in self.ev2.get_entries():
                if x.get_values == ['omega'] and y.get_values != ['omega']:
                    prob = x.get_probability * y.get_probability
                    self.evout.add_entry(BasisMeasure(y.get_values, prob))
                elif y.get_values == ['omega'] and x.get_values != ['omega']:
                    prob = x.get_probability * y.get_probability
                    self.evout.add_entry(BasisMeasure(x.get_values, prob))
                elif y.get_values == ['omega'] and x.get_values == ['omega']:
                    prob = x.get_probability * y.get_probability
                    self.evout.add_entry(BasisMeasure(['omega'], prob))
                else:
                    valout = []
                    for a in y.get_values:
                        if a in x.get_values:
                            valout.append(a)
                    if valout == []:
                        # do shit
                    else:
                        # unify and do other shit



        # add stuff together
        # refactor when smth is empty

    def get_output(self):
        return self.evout
