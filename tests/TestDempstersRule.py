from DempsterRule import DempsterRule
from Evidence import Evidence
from BasisMeasure import BasisMeasure

ev5 = Evidence(None, None)
ev5.add_entry(BasisMeasure(['anger', 'joy'], 0.5))
ev5.add_entry(BasisMeasure(['disgust', 'joy'], 0.4))
ev5.add_entry(BasisMeasure(['omega'], 0.1))
ev6 = Evidence(None, None)
ev6.add_entry(BasisMeasure(['fear', 'sorrow', 'joy'], 0.8))
ev6.add_entry(BasisMeasure(['omega'], 0.2))
demp3 = DempsterRule(ev6, ev5)

def test_calc_demp():
    ev1 = Evidence(None, None)
    ev1.add_entry(BasisMeasure(['anger', 'joy'], 0.7))
    ev1.add_entry(BasisMeasure(['omega'], 0.3))
    ev2 = Evidence(None, None)
    ev2.add_entry(BasisMeasure(['sadness', 'joy'], 0.4))
    ev2.add_entry(BasisMeasure(['omega'], 0.6))
    demp1 = DempsterRule(ev1, ev2)
    expected1 = [BasisMeasure(['joy'], 0.28), BasisMeasure(['anger', 'joy'], 0.42),
                 BasisMeasure(['sadness', 'joy'], 0.12), BasisMeasure(['omega'], 0.18)]
    assert demp1.get_output().get_entries()[3].get_probability() == expected1[3].get_probability()

def test_calc_empty():
    ev3 = Evidence(None, None)
    ev3.add_entry(BasisMeasure(['joy'], 0.7))
    ev3.add_entry(BasisMeasure(['omega'], 0.3))
    ev4 = Evidence(None, None)
    ev4.add_entry(BasisMeasure(['fear'], 0.6))
    ev4.add_entry(BasisMeasure(['omega'], 0.4))
    demp2 = DempsterRule(ev4, ev3)
    expected2 = [BasisMeasure(['fear'], 0.31034483), BasisMeasure(['joy'], 0.48275862),
                 BasisMeasure(['omega'], 0.20689655)]
    assert round(demp2.get_output().get_entries()[0].get_probability(), 5) == round(expected2[0].get_probability(), 5)

def test_calc_unification():
    expected = [BasisMeasure(['joy'], 0.72), BasisMeasure(['fear', 'sorrow', 'joy'], 0.08),
                 BasisMeasure(['anger', 'joy'], 0.1), BasisMeasure(['disgust', 'joy'], 0.08), BasisMeasure(['omega'], 0.02)]
    assert round(demp3.get_output().get_entries()[1].get_probability(), 5) == round(expected[1].get_probability(), 5)

def test_calc_plausibility():
    expected = [['joy', 0.98], ['fear', 0.08], ['sorrow', 0.08], ['anger', 0.1], ['disgust', 0.08]]
    # expected with omega:
    # expected3 = [['joy', 1], ['fear', 0.1], ['sorrow', 0.1], ['anger', 0.12], ['disgust', 0.1]]
    assert all(demp3.cal_plausibility()) == all(expected)

def test_calc_belief():
    expected = [['joy', 0.72], ['fear', 0], ['sorrow', 0], ['anger', 0], ['disgust', 0]]
    assert all(demp3.cal_belief()) == all(expected)