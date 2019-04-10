from Entry import Entry

valuesreg = [2, 3, 4]
valuesempty = []
probability5 = 0.5
probability1 = 0.1


# test if a regular instantiation with a value list also returns those values
def test_valuelist_regular():
    assert (Entry(valuesreg, probability5).get_focalset() == valuesreg)

# test if an empty value list is possible
def test_valuelist_empty():
    assert (Entry(valuesempty, probability5).get_focalset() == valuesempty)

# test if a regular instntiation with some probability also returns this probability
def test_probability_regular():
    assert (Entry(valuesreg, probability5).get_confidence() == probability5)

# test if the value-setter works properly
def test_setvalue():
    e = Entry(valuesreg, probability5)
    e.set_focalset(valuesempty)
    assert (e.get_focalset() == valuesempty)

# test if the probability-setter works properly
def test_setprobability():
    e = Entry(valuesreg, probability5)
    e.set_confidence(probability1)
    assert (e.get_confidence() == probability1)

# to run tests: py.test TestBasisMeasure.py