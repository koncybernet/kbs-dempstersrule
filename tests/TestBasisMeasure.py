from Evidence import BasisMeasure

entry = 'test'


def test_addandgetentry():
    bm = BasisMeasure(None, None)
    bm.add_entry(entry)
    assert (bm.get_entries() == ['test'])

def test_emptyconstructor():
    assert (BasisMeasure(None, None).get_entries() == [])

# TODO test constructing of entries with other way


# when done run py.test TestBasisMeasure.py