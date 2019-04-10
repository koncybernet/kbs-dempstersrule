# class to implement an Evidence, with entries in this list being a Basis Measure.

from Entry import Entry

class Evidence:
    # the constructor has two options, either it is instantiated empty, being the case if the Evidence is the
    # accumulation of two prior Evidences, or with feature and size, which will be mapped in the seperate Excel sheet. This
    # is the case when in the first step all columns from the analysis-data are read and converted to an Evidence.
    def __init__(self, focalset, confidence):
        if confidence is None or focalset is None: 
            self.entrylist = []
        else:
            self.entrylist = [Entry(focalset, confidence), Entry(['omega'], 1 - confidence)]

    def add_entry(self, entry):
        self.entrylist.append(entry)

    def get_entries(self):
        return self.entrylist

    def delete_entry(self, index):
        self.entrylist.remove(index)

    def cal_plausibility(self):
        # TODO wird Omega miteinberechnet?
        all_emotions = []
        output = []
        for x in self.entrylist:
            for y in x.get_focalset():
                if y not in all_emotions:
                    all_emotions.append(y)
        all_emotions.remove('omega')
        for e in all_emotions:
            plausibility = 0
            for f in self.entrylist:
                for g in f.get_focalset():
                    if e in g:
                        plausibility += f.get_confidence()
            output.append([e, plausibility])
        return output

    # method to calculate the belief for all emotions present
    def cal_belief(self):
        all_emotions = []
        output = []
        for x in self.entrylist:
            for y in x.get_focalset():
                if y not in all_emotions:
                    all_emotions.append(y)
        all_emotions.remove('omega')
        for e in all_emotions:
            belief = 0
            for f in self.entrylist:
                if [e] == f.get_focalset():
                    belief += f.get_confidence()
            output.append([e, belief])
        return output
