from DempsterRule import DempsterRule
from BasisMeasure import BasisMeasure
from Entry import Entry

ev5 = BasisMeasure(None, None)
ev5.add_entry(Entry(['anger', 'joy'], 0.5))
ev5.add_entry(Entry(['disgust', 'joy'], 0.4))
ev5.add_entry(Entry(['omega'], 0.1))
ev6 = BasisMeasure(None, None)
ev6.add_entry(Entry(['fear', 'sorrow', 'joy'], 0.8))
ev6.add_entry(Entry(['omega'], 0.2))
demp3 = DempsterRule(ev6, ev5)

# test if output evidence is calculated correctly
def test_calc_demp():
    ev1 = BasisMeasure(None, None)
    ev1.add_entry(Entry(['anger', 'joy'], 0.7))
    ev1.add_entry(Entry(['omega'], 0.3))
    ev2 = BasisMeasure(None, None)
    ev2.add_entry(Entry(['sadness', 'joy'], 0.4))
    ev2.add_entry(Entry(['omega'], 0.6))
    demp1 = DempsterRule(ev1, ev2)
    expected1 = [Entry(['joy'], 0.28), Entry(['anger', 'joy'], 0.42),
                 Entry(['sadness', 'joy'], 0.12), Entry(['omega'], 0.18)]
    assert demp1.get_output().get_entries()[3].get_confidence() == expected1[3].get_confidence()

# test if refactoring is done when an output basis measure is empty
def test_calc_empty():
    ev3 = BasisMeasure(None, None)
    ev3.add_entry(Entry(['joy'], 0.7))
    ev3.add_entry(Entry(['omega'], 0.3))
    ev4 = BasisMeasure(None, None)
    ev4.add_entry(Entry(['fear'], 0.6))
    ev4.add_entry(Entry(['omega'], 0.4))
    demp2 = DempsterRule(ev4, ev3)
    expected2 = [Entry(['fear'], 0.31034483), Entry(['joy'], 0.48275862),
                 Entry(['omega'], 0.20689655)]
    assert round(demp2.get_output().get_entries()[0].get_confidence(), 5) == round(expected2[0].get_confidence(), 5)

# test if two basismeasures with same content are added together
def test_calc_unification():
    expected = [Entry(['joy'], 0.72), Entry(['fear', 'sorrow', 'joy'], 0.08),
                Entry(['anger', 'joy'], 0.1), Entry(['disgust', 'joy'], 0.08), Entry(['omega'], 0.02)]
    assert round(demp3.get_output().get_entries()[1].get_confidence(), 5) == round(expected[1].get_confidence(), 5)
