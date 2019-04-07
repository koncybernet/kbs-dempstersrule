from Evidence import Evidence

entry = 'test'

# test if entries are appended correctly
def test_addandgetentry():
    bm = Evidence(None, None)
    bm.add_entry(entry)
    assert (bm.get_entries() == ['test'])

# test if the empty constructor logic is working
def test_emptyconstructor():
    assert (Evidence(None, None).get_entries() == [])

# test if the construction with values from table works accordingly
def test_tableconstructor():
    # TODO test constructing of entries with other way
    assert 1 == 1

# when done run py.test TestEvidence.py