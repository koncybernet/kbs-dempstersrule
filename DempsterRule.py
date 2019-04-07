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
                    for c in self.evout.get_entries():
                        if set(y.get_values()) == set(c.get_values()):
                            c.set_probability(c.get_probability + prob)
                        else:
                            self.evout.add_entry(BasisMeasure(y.get_values(), prob))
                elif y.get_values() == ['omega'] and x.get_values() != ['omega']:
                    for c in self.evout.get_entries():
                        if set(x.get_values()) == set(c.get_values()):
                            c.set_probability(c.get_probability + prob)
                        else:
                            self.evout.add_entry(BasisMeasure(y.get_values(), prob))
                elif y.get_values() == ['omega'] and x.get_values() == ['omega']:
                    for c in self.evout.get_entries():
                        if c.get_values() == ['omega']:
                            c.set_probability(c.get_probability + prob)
                        else:
                            self.evout.add_entry(BasisMeasure(['omega'], prob))
                else:
                    valout = []
                    for a in y.get_values():
                        if a in x.get_values():
                            valout.append(a)
                    if valout == []:
                        # check if existing and if exists already just calculate new prob
                        self.evout.add_entry(BasisMeasure(['empty'], prob))
                    else:
                        # check if existing and if exists already just calculate new prob
                        self.evout.add_entry(BasisMeasure(valout, prob))

        probofempty = 0
        for ind, m in enumerate(self.evout.get_entries()):
            if m.get_values() == ['empty']:
                probofempty += m.get_probability()
                self.evout.delete_entry(m)
        factor = 1 / (1 - probofempty)
        for n in self.evout.get_entries():
            n.set_probability(n.get_probability()*factor)

        #test if sum of all probabilites is still 1
        sum = 0
        for o in self.evout.get_entries():
            sum += o.get_probability()
        if abs(sum - 1)>0.0000000001:
            raise ValueError('the corrected probabilites do not equal one anymore, something is wrong ' + str(sum))


    def get_output(self):
        return self.evout
