from DempsterRule import DempsterRule
from Evidence import Evidence
from BasisMeasure import BasisMeasure

ev1 = Evidence(None, None)
ev1.add_entry(BasisMeasure(['anger', 'joy'], 0.7))
ev1.add_entry(BasisMeasure(['omega'], 0.3))
ev2 = Evidence(None, None)
ev2.add_entry(BasisMeasure(['sadness', 'joy'], 0.4))
ev2.add_entry(BasisMeasure(['omega'], 0.6))
demp1 = DempsterRule(ev1, ev2)
expected1 = [BasisMeasure(['joy'], 0.28), BasisMeasure(['anger', 'joy'], 0.42), BasisMeasure(['sadness', 'joy'], 0.12), BasisMeasure(['omega'], 0.18)]

ev3 = Evidence(None, None)
ev3.add_entry(BasisMeasure(['joy'], 0.7))
ev3.add_entry(BasisMeasure(['omega'], 0.3))
ev4 = Evidence(None, None)
ev4.add_entry(BasisMeasure(['fear'], 0.6))
ev4.add_entry(BasisMeasure(['omega'], 0.4))
demp2 = DempsterRule(ev4, ev3)
expected2 = [BasisMeasure(['fear'], 0.31034483), BasisMeasure(['joy'], 0.48275862), BasisMeasure(['omega'], 0.20689655)]

def test_calc_demp():
    assert demp1.get_output().get_entries()[3].get_probability() == expected1[3].get_probability()

def test_calc_empty():
    assert round(demp2.get_output().get_entries()[0].get_probability(), 5) == round(expected2[0].get_probability(), 5)

