from BasisMeasure import BasisMeasure
from DempsterRule import DempsterRule
from Entry import Entry

ev5 = BasisMeasure(None, None)
ev5.add_entry(Entry(['anger', 'joy'], 0.5))
ev5.add_entry(Entry(['disgust', 'joy'], 0.4))
ev5.add_entry(Entry(['omega'], 0.1))
ev6 = BasisMeasure(None, None)
ev6.add_entry(Entry(['fear', 'sorrow', 'joy'], 0.8))
ev6.add_entry(Entry(['omega'], 0.2))
demp3 = DempsterRule(ev6, ev5).get_output()


entry = 'test'

# test if entries are appended correctly
def test_addandgetentry():
    bm = BasisMeasure(None, None)
    bm.add_entry(entry)
    assert (bm.get_entries() == ['test'])

# test if the empty constructor logic is working
def test_emptyconstructor():
    assert (BasisMeasure(None, None).get_entries() == [])

# test if plausibility is calculated correctly
def test_calc_plausibility():
    # expected = [['joy', 0.98], ['fear', 0.08], ['sorrow', 0.08], ['anger', 0.1], ['disgust', 0.08]]
    # expected with omega:
    expected = [['joy', 1], ['fear', 0.1], ['sorrow', 0.1], ['anger', 0.12], ['disgust', 0.1]]
    assert all(demp3.cal_plausibility()) == all(expected)

# test if belief is calculated correctly
def test_calc_belief():
    expected = [['joy', 0.72], ['fear', 0], ['sorrow', 0], ['anger', 0], ['disgust', 0]]
    assert all(demp3.cal_belief()) == all(expected)




# when done run py.test TestBasisMeasure.py