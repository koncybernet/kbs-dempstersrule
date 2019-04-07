# class to implement the functionality of the Dempster Rule, accumulating two BasisMeasures into
# one output Basis Measure

from Evidence import Evidence
from BasisMeasure import BasisMeasure

class DempsterRule:
    def __init__(self, ev1, ev2):
        self.ev1 = ev1
        self.ev2 = ev2
        self.evout = Evidence(None, None)

        # for each cell of the 'output table', create an entry in the output consisting of
        # the values/emotions and the probability for those values/emotions. In every case,
        # it is checked whether a BasisMeasure with exactly those values exists already. Then,
        # no new BasisMeasure is created and instead the probability of the current object is added
        # to the already existing one.
        for x in self.ev1.get_entries():
            for y in self.ev2.get_entries():
                # calculate output-probability beforehand because it is needed in every case
                prob = float(x.get_probability()) * float(y.get_probability())
                # case 1 if one of the two inputs is omega
                if x.get_values() == ['omega'] and y.get_values() != ['omega']:
                    exists = False
                    for c in self.evout.get_entries():
                        if set(y.get_values()) == set(c.get_values()):
                            c.set_probability(c.get_probability() + prob)
                            exists = True
                    if not exists:
                        self.evout.add_entry(BasisMeasure(y.get_values(), prob))
                # case 2 if one of the two inputs is omega
                elif y.get_values() == ['omega'] and x.get_values() != ['omega']:
                    exists = False
                    for c in self.evout.get_entries():
                        if set(x.get_values()) == set(c.get_values()):
                            c.set_probability(c.get_probability() + prob)
                            exists = True
                    if not exists:
                        self.evout.add_entry(BasisMeasure(x.get_values(), prob))
                # case if both of the input values are omega
                elif y.get_values() == ['omega'] and x.get_values() == ['omega']:
                    # no backlooking comparison needed since there is always just one omega output field
                    self.evout.add_entry(BasisMeasure(['omega'], prob))
                #case if no input is omega, first check if the two inputs have emotions in common
                else:
                    valout = []
                    for a in y.get_values():
                        if a in x.get_values():
                            valout.append(a)
                    # if the inputs have no emotions in common, create 'empty' BasisMeasure
                    if valout == []:
                        exists = False
                        for c in self.evout.get_entries():
                            if c.get_values() == ['empty']:
                                c.set_probability(c.get_probability() + prob)
                                exists = True
                        if not exists:
                            self.evout.add_entry(BasisMeasure(['empty'], prob))
                    # is the inputs have emotions in common, create BasisMeasure with shared emotions
                    else:
                        exists = False
                        for c in self.evout.get_entries():
                            if set(valout) == set(c.get_values()):
                                c.set_probability(c.get_probability() + prob)
                                exists = True
                        if not exists:
                            self.evout.add_entry(BasisMeasure(valout, prob))

        # check if there is an empty element in the output. if so, determine the probability of the empty
        # element and with the formula 1/(1-k) recalculate the remaining probabilities
        probofempty = 0
        for ind, m in enumerate(self.evout.get_entries()):
            if m.get_values() == ['empty']:
                probofempty += m.get_probability()
                self.evout.delete_entry(m)
        factor = 1 / (1 - probofempty)
        for n in self.evout.get_entries():
            n.set_probability(n.get_probability()*factor)

        #test if sum of all probabilites is still 1 as a check
        sum = 0
        for o in self.evout.get_entries():
            sum += o.get_probability()
        if abs(sum - 1)>0.0000000001:
            raise ValueError('the corrected probabilites do not equal one anymore, something is wrong ' + str(sum))


    def get_output(self):
        return self.evout

    # method to calculate the belief for all emotions present
    def cal_belief(self):
        all_emotions = []
        output = []
        for x in self.evout.get_entries():
            for y in x.get_values():
                if y not in all_emotions:
                    all_emotions.append(y)
        all_emotions.remove('omega')
        for e in all_emotions:
            belief = 0
            for f in self.evout.get_entries():
                if [e] == f:
                    belief += f.get_probability()
            output.append([e, belief])
        return output
