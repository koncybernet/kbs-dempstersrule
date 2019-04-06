from Evidence import Evidence
from BasisMeasure import BasisMeasure

class DempsterRule:
    def __init__(self, ev1, ev2):
        self.ev1 = ev1
        self.ev2 = ev2
        self.evout = Evidence(None, None)

        for x in self.ev1.get_entries():
            for y in self.ev2.get_entries():
                prob = float(x.get_probability()) * float(y.get_probability())
                if x.get_values() == ['omega'] and y.get_values() != ['omega']:
                    self.evout.add_entry(BasisMeasure(y.get_values(), prob))
                elif y.get_values() == ['omega'] and x.get_values() != ['omega']:
                    self.evout.add_entry(BasisMeasure(x.get_values(), prob))
                elif y.get_values() == ['omega'] and x.get_values() == ['omega']:
                    self.evout.add_entry(BasisMeasure(['omega'], prob))
                else:
                    valout = []
                    for a in y.get_values():
                        if a in x.get_values():
                            valout.append(a)
                    if valout == []:
                        self.evout.add_entry(BasisMeasure([], prob))
                    else:
                        self.evout.add_entry(BasisMeasure(valout, prob))

        # add stuff together


        # refactor when smth is empty

    def get_output(self):
        return self.evout
