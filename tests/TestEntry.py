from BasisMeasure import Entry

valuesreg = [2, 3, 4]
valuesempty = []
probability5 = 0.5
probability1 = 0.1


def test_valuelist_regular():
    assert (Entry(valuesreg, probability5).get_values() == valuesreg)

def test_valuelist_empty():
    assert (Entry(valuesempty, probability5).get_values() == valuesempty)

def test_probability_regular():
    assert (Entry(valuesreg, probability5).get_probability() == probability5)

def test_setvalue():
    e = Entry(valuesreg, probability5)
    e.set_values(valuesempty)
    assert (e.get_values() == valuesempty)

def test_setprobability():
    e = Entry(valuesreg, probability5)
    e.set_probability(probability1)
    assert (e.get_probability() == probability1)

# when done run py.test TestEntry.py