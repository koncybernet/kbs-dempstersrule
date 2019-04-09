# takes a list of facial features (traits) found in file and the file itself and returns an object containing
# subsets of emotions and the confidence for each subset
def complete_conversion(traits, line):
    sizes = number_to_size(traits, line)
    emotions = size_to_emotion(sizes)

    return emotions


# takes a list of traits and one line of numbers (extracted from csv) and returns an object with a mapping of trait -> size
def number_to_size(traits, numbers):

    normalized_numbers = {}
    height_of_frame = numbers[traits.index('ylow')]

    # for all values in line of numbers lookup trait, normalize its number and store it in object
    for trait in traits:
        if trait_is_relevant(trait) == True and numbers[traits.index(trait)] != '':
            normalized_numbers[trait] = normalize_number(height_of_frame, numbers[traits.index(trait)], trait)


    result = {}
    # for every trait, lookup its size and add it to the result object
    for trait in normalized_numbers:
        result[trait] = number_to_size_table_lookup(trait, normalized_numbers[trait])

    return(result)


# takes a trait and returnsa boolean stating wether or not the trait is a facial feature
def trait_is_relevant(trait):
    relevant_traits = ['fob', 'lea', 'lbd', 'rea', 'rbd', 'hnc', 'vnc', 'lcw', 'rcw', 'ma']

    if trait in relevant_traits:
        return True
    else:
        return False


# takes the height of the current frame, the trait value and the trait
# returns a normalized number
def normalize_number(y, number, trait):
    if number is None or number == '':
        return ''
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
    normalized_number = round((int(number) / int(y)) * int(trait_multiplier_table[trait]))
    return(normalized_number)


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
        return('s')
    elif size_table[trait]['m'][0] <= value and size_table[trait]['m'][1] > value:
        return('m')
    else:
        return('l') 


# takes an object with a mapping of trait -> size and returns all possible emotions for that trait and their confidence
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

     # result object
    result = {}

    # store all valid emotions and their confidence in set
    for trait in size_object:
        emotions = table[trait][size_object[trait]]
        if emotions != []: 
            result[trait] = {}        
            result[trait]['emotions'] = emotions
            result[trait]['value'] = round(len(emotions) / (5 - len(emotions)), 5)

    return(result)
