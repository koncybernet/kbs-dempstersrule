# class to implement an Evidence, with entries in this list being a Basis Measure.

from table_lookups import size_to_emotion

class Evidence:
    # the constructor has two options, either it is instantiated empty, being the case if the Evidence is the
    # accumulation of two prior Evidences, or with feature and size, which will be mapped in the seperate Excel sheet. This
    # is the case when in the first step all columns from the analysis-data are read and converted to an Evidence.
    def __init__(self, feature, size):
        if feature or size is None:
            self.entrylist = []
        else:
            self.entrylist = []
            # TODO
            # get list of emotions from lookup
            # append list of emotions with prob
            # append omegaobject with 1 - prob

    def add_entry(self, entry):
        self.entrylist.append(entry)

    def get_entries(self):
        return self.entrylist

    def delete_entry(self, index):
        self.entrylist.remove(index)