from DempsterRule import DempsterRule
from Evidence import Evidence
from BasisMeasure import BasisMeasure

ev1 = Evidence(None, None)
ev1.add_entry(BasisMeasure(['anger', 'joy'], 0.7))
ev1.add_entry(BasisMeasure(['omega'], 0.3))
ev2 = Evidence(None, None)
ev2.add_entry(BasisMeasure(['sadness', 'joy'], 0.4))
ev2.add_entry(BasisMeasure(['omega'], 0.6))
demp = DempsterRule(ev1, ev2)

expected = {BasisMeasure(['joy'], 0.28), BasisMeasure(['anger', 'joy'], 0.42), BasisMeasure(['sadness', 'joy'], 0.12), BasisMeasure(['omega'], 0.18)}

def test_calc_demp():
    assert (demp.get_output == expected)