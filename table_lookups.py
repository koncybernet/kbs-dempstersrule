def size_to_emotion(size_object):
    # example input: {
    #   'fob': 's',
    #   'lea': 'm',
    #   'rea': 'm',
    #   ...
    # }

    # table to look up traits
    table = {
        'fob': {
            's': ['neutral', 'disgust'],
            'm': ['joy'],
            'l': ['sorrow', 'fear']
        },
        'lea': {
            's': ['sorrow', 'disgust'],
            'm': ['neutral', 'sorrow'],
            'l': ['fear', 'joy']
        },
        'lbd': {
            's': ['disgust'],
            'm': ['neutral', 'sorrow'],
            'l': ['fear', 'joy']
        },
        'rea': {
            's': ['sorrow', 'disgust'],
            'm': ['neutral', 'sorrow'],
            'l': ['fear', 'joy']
        },
        'rbd': {
            's': ['disgust'],
            'm': ['neutral', 'sorrow'],
            'l': ['fear', 'joy']
        },
        'hnc': {
            's': [],
            'm': [],
            'l': ['fear']
        },
        'vnc': {
            's': [],
            'm': [],
            'l': []
        },
        'lcw': {
            's': ['sorrow'],
            'm': ['sorrow', 'joy', 'disgust'],
            'l': ['joy']
        },
        'rcw': {
            's': ['sorrow'],
            'm': ['sorrow', 'joy', 'disgust'],
            'l': ['joy']
        },
        'ma': {
            's': [],
            'm': [],
            'l': ['fear']
        }
    }

    # sets can not contain duplicates as opposed to lists
    emotions = set(())

    # store all valid emotions in set
    for trait in size_object:
        emotions.update(table[trait][size_object[trait]])

    # result object
    result = {}

    # store all valid emotions and their value in result object
    result['emotions'] = emotions
    result['value'] = len(emotions) / (5 - len(emotions))

    print(result)
    return(result)


def number_to_size(numbers):

    normalized_numbers = {}

    for i in range(5, 14):
        trait = lookup_trait_by_index(i)
        normalized_numbers[trait] = normalize_number(i, numbers[4], numbers[i], trait)

    size_table = {
        'fob': {
            's': [0, 100],
            'm': [100, 200],
            'l': [200,  -1]
        },
        'lea': {
            's': [0, 3],
            'm': [3, 7],
            'l': [7, -1]
        },
        'lbd': {
            's': [0, 3],
            'm': [3, 7],
            'l': [7, -1]
        },
        'rea': {
            's': [0, 3],
            'm': [3, 7],
            'l': [7, -1]
        },
        'rbd': {
            's': [0, 3],
            'm': [3, 7],
            'l': [7, -1]
        },
        'hnc': {
            's': [0, 8],
            'm': [8, 18],
            'l': [18, -1]
        },
        'vnc': {
            's': [0, 8],
            'm': [8, 19],
            'l': [19, -1]
        },
        'lcw': {
            's': [0, 3],
            'm': [3, 7],
            'l': [7, -1]
        },
        'rcw': {
            's': [0, 3],
            'm': [3, 7],
            'l': [7, -1]
        },
        'ma': {
            's': [0, 7],
            'm': [7, 14],
            'l': [14, -1]
        }
    }

    for trait in normalized_numbers:

    


def normalize_number(i, y, number, trait):
    trait_multiplier_table = {
        'fob': 1,
        'lea': 100,
        'lbd': 100,
        'rea': 100,
        'rbd': 100,
        'hnc': 1000,
        'vnc': 1000,
        'lcw': 100,
        'rcw': 100,
        'ma': 100
    }

    normalized_number = round((number / y) * trait_multiplier_table[trait])
    return(normalized_number)


def lookup_trait_by_index(i):
    trait_switch = {
        5: 'fob',
        6: 'lea',
        7: 'lbd',
        8: 'rea',
        9: 'rbd',
        10: 'hnc',
        11: 'vnc',
        12: 'lcw',
        13: 'rcw',
        14: 'ma'
    }

    return(trait_switch[i])











object = {
    'fob': 'm',
    'lea': 'l',
    'rea': 'l',
    'lbd': 'l',
    'rbd': 'l',
    'hnc': 'l',
    'vnc': 'l',
    'lcw': 'l',
    'rcw': 'l',
    'ma': 'l'
}

size_to_emotion(object)

