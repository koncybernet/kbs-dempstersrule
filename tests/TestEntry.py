from Entry import Entry

def test_valuelist_regular():
    values = [2, 3, 4]
    assert( Entry(values).get_values() == values )

def test_valuelist_empty():
    values = []
    assert (Entry(values).get_values() == values)

# when done run py.test TestEntry.py