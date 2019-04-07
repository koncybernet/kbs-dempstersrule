import data_conversion

def test_lookup_trait_by_index():
    assert data_conversion.lookup_trait_by_index(5) == 'fob'

def test_normalize_number():
    assert data_conversion.normalize_number(500, 10, 'rea') == 2

def test_number_to_size_table_lookup():
    assert data_conversion.number_to_size_table_lookup('hnc', 12) == 'm'

def test_number_to_size():
    test_numbers = [1, 0, 0, 300, 500, 30000, 24, 22, 22, 21, 5, 3, 10, 10, 84]
    expected_object = {
        'fob': 's',
        'lea': 'm',
        'lbd': 'm',
        'rea': 'm',
        'rbd': 'm',
        'hnc': 'm',
        'vnc': 's',
        'lcw': 's',
        'rcw': 's',
        'ma': 'l'
    }

    assert all(expected_object) == all(data_conversion.number_to_size(test_numbers))

def test_size_to_emotion():
    test_object = {
        'fob': 's',
        'lea': 'm',
        'lbd': 'm',
        'rea': 'm',
        'rbd': 'm',
        'hnc': 'm',
        'vnc': 's',
        'lcw': 's',
        'rcw': 's',
        'ma': 'l'
    }

    expected_object = {
        'fob': {
            'emotions': ['neutral', 'disgust'],
            'value': 0.66667
        },
        'lea': {
            'emotions': ['neutral', 'sorrow'],
            'value': 0.66667
        },
        'lbd': {
            'emotions': ['neutral', 'sorrow'],
            'value': 0.66667
        },
        'rea': {
            'emotions': ['neutral', 'sorrow'],
            'value': 0.66667
        },
        'rbd': {
            'emotions': ['neutral', 'sorrow'],
            'value': 0.66667
        },
        'hnc': {
            'emotions': [],
            'value': 0
        },
        'vnc': {
            'emotions': [],
            'value': 0
        },
        'lcw': {
            'emotions': ['sorrow'],
            'value': 0.25
        },
        'rcw': {
            'emotions': ['sorrow'],
            'value': 0.25
        },
        'ma': {
            'emotions': ['fear'],
            'value': 0.25
        }
    }

    assert all(expected_object) == all(data_conversion.size_to_emotion(test_object))