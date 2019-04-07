# takes an object with a mapping of trait -> size and returns all possible emotions for that trait and their value
def size_to_emotion(size_object):
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



# takes one line of numbers (extracted from csv) and return an object with a mapping of trait -> size
def number_to_size(numbers):

    normalized_numbers = {}

    # for all values in line of numbers lookup trait, normalize its number and store it in object
    for i in range(5, 14):
        trait = lookup_trait_by_index(i)
        normalized_numbers[trait] = normalize_number(i, numbers[4], numbers[i], trait)


    result = {}
    # for every trait, lookup its size and add it to the result object
    for trait in normalized_numbers:
        result[trait] = number_to_size_table_lookup(trait, normalized_numbers[trait])
    

# takes a trait and its value and returns the size
def number_to_size_table_lookup(trait, value):
    size_table = {
        'fob': {
            's': [0, 100],
            'm': [100, 200],
            'l': [200,]
        },
        'lea': {
            's': [0, 3],
            'm': [3, 7],
            'l': [7,]
        },
        'lbd': {
            's': [0, 3],
            'm': [3, 7],
            'l': [7,]
        },
        'rea': {
            's': [0, 3],
            'm': [3, 7],
            'l': [7,]
        },
        'rbd': {
            's': [0, 3],
            'm': [3, 7],
            'l': [7,]
        },
        'hnc': {
            's': [0, 8],
            'm': [8, 18],
            'l': [18,]
        },
        'vnc': {
            's': [0, 8],
            'm': [8, 19],
            'l': [19,]
        },
        'lcw': {
            's': [0, 3],
            'm': [3, 7],
            'l': [7,]
        },
        'rcw': {
            's': [0, 3],
            'm': [3, 7],
            'l': [7,]
        },
        'ma': {
            's': [0, 7],
            'm': [7, 14],
            'l': [14]
        }
    }

    # check number for size and return it
    if size_table[trait]['s'][0] <= value and size_table[trait]['s'][1] > value:
        return 's'
    elif size_table[trait]['m'][0] <= value and size_table[trait]['s'][1] > value:
        return 'm'
    else:
        return 'l' 


# takes an index according to the line of numbers, the height of the current frame, the trait value and the trait
# returns a normalized number
def normalize_number(i, y, number, trait):
    # multiplier to get integers that are separable by rounding
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

    # normalize number with frame height, include multiplier for trait and round to next integer
    normalized_number = round((number / y) * trait_multiplier_table[trait])
    return(normalized_number)


# takes an index and returns the trait that belongs to the index
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
