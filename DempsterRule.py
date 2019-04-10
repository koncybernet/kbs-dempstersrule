# class to implement the functionality of the Dempster Rule, accumulating two BasisMeasures into
# one output Basis Measure

from BasisMeasure import BasisMeasure
from Entry import Entry

class DempsterRule:
    def __init__(self, bm1, bm2):
        self.bm1 = bm1
        self.bm2 = bm2
        self.bmout = BasisMeasure(None, None)

        # for each cell of the 'output table', create an entry in the output consisting of
        # the values/emotions and the probability for those values/emotions. In every case,
        # it is checked whether a BasisMeasure with exactly those values exists already. Then,
        # no new BasisMeasure is created and instead the probability of the current object is added
        # to the already existing one.
        for x in self.bm1.get_entries():
            for y in self.bm2.get_entries():
                # calculate output-probability beforehand because it is needed in every case
                prob = float(x.get_confidence()) * float(y.get_confidence())
                # case 1 if one of the two inputs is omega
                if x.get_focalset() == ['omega'] and y.get_focalset() != ['omega']:
                    exists = False
                    for c in self.bmout.get_entries():
                        if set(y.get_focalset()) == set(c.get_focalset()):
                            c.set_confidence(c.get_confidence() + prob)
                            exists = True
                    if not exists:
                        self.bmout.add_entry(Entry(y.get_focalset(), prob))
                # case 2 if one of the two inputs is omega
                elif y.get_focalset() == ['omega'] and x.get_focalset() != ['omega']:
                    exists = False
                    for c in self.bmout.get_entries():
                        if set(x.get_focalset()) == set(c.get_focalset()):
                            c.set_confidence(c.get_confidence() + prob)
                            exists = True
                    if not exists:
                        self.bmout.add_entry(Entry(x.get_focalset(), prob))
                # case if both of the input values are omega
                elif y.get_focalset() == ['omega'] and x.get_focalset() == ['omega']:
                    # no backlooking comparison needed since there is always just one omega output field
                    self.bmout.add_entry(Entry(['omega'], prob))
                #case if no input is omega, first check if the two inputs have emotions in common
                else:
                    valout = []
                    for a in y.get_focalset():
                        if a in x.get_focalset():
                            valout.append(a)
                    # if the inputs have no emotions in common, create 'empty' BasisMeasure
                    if valout == []:
                        exists = False
                        for c in self.bmout.get_entries():
                            if c.get_focalset() == ['empty']:
                                c.set_confidence(c.get_confidence() + prob)
                                exists = True
                        if not exists:
                            self.bmout.add_entry(Entry(['empty'], prob))
                    # is the inputs have emotions in common, create BasisMeasure with shared emotions
                    else:
                        exists = False
                        for c in self.bmout.get_entries():
                            if set(valout) == set(c.get_focalset()):
                                c.set_confidence(c.get_confidence() + prob)
                                exists = True
                        if not exists:
                            self.bmout.add_entry(Entry(valout, prob))

        # check if there is an empty element in the output. if so, determine the probability of the empty
        # element and with the formula 1/(1-k) recalculate the remaining probabilities
        probofempty = 0
        for ind, m in enumerate(self.bmout.get_entries()):
            if m.get_focalset() == ['empty']:
                probofempty += m.get_confidence()
                self.bmout.delete_entry(m)
        factor = 1 / (1 - probofempty)
        for n in self.bmout.get_entries():
            n.set_confidence(n.get_confidence() * factor)

        #test if sum of all probabilites is still 1 as a check
        sum = 0
        for o in self.bmout.get_entries():
            sum += o.get_confidence()
        if abs(sum - 1)>0.0000000001:
            raise ValueError('the corrected probabilites do not equal one anymore, something is wrong ' + str(sum))


    def get_output(self):
        return self.bmout
