from BasisMeasure import BasisMeasure

valuesreg = [2, 3, 4]
valuesempty = []
probability5 = 0.5
probability1 = 0.1


# test if a regular instantiation with a value list also returns those values
def test_valuelist_regular():
    assert (BasisMeasure(valuesreg, probability5).get_values() == valuesreg)

# test if an empty value list is possible
def test_valuelist_empty():
    assert (BasisMeasure(valuesempty, probability5).get_values() == valuesempty)

# test if a regular instntiation with some probability also returns this probability
def test_probability_regular():
    assert (BasisMeasure(valuesreg, probability5).get_probability() == probability5)

# test if the value-setter works properly
def test_setvalue():
    e = BasisMeasure(valuesreg, probability5)
    e.set_values(valuesempty)
    assert (e.get_values() == valuesempty)

# test if the probability-setter works properly
def test_setprobability():
    e = BasisMeasure(valuesreg, probability5)
    e.set_probability(probability1)
    assert (e.get_probability() == probability1)

# to run tests: py.test TestBasisMeasure.py