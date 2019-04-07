from table_lookups import size_to_emotion

# the measure list in this excercise equals the an m, so m1 for the FOB (Stirnfalte)
class Evidence:
    def __init__(self, feature, size):
        if feature or size is None:
            self.entrylist = []
        else:
            self.entrylist = []
            # get list of emotions from lookup
            # append list of emotions with prob
            # append omegaobject with 1 - prob

    def add_entry(self, entry):
        self.entrylist.append(entry)

    def get_entries(self):
        return self.entrylist

    def delete_entry(self, index):
        self.entrylist.remove(index)