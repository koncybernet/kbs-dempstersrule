def data_cleansing(traits, line):
    # normalized_numbers = {}
    confidence = {}
    height_of_frame = line[traits.index('ylow')]

    # for all values in line of numbers lookup trait, normalize its number and store it in object
    for trait in traits:
        if trait_is_relevant(trait) == True and line[traits.index(trait)] != '':
            # normalize number
            normalized = normalize_number(height_of_frame, line[traits.index(trait)], trait)
            # get confidence and size
            confidence[trait] = get_confidence(trait, normalized)

    emotions = size_to_emotion(confidence)
    # print(emotions)
    return emotions        

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


def get_size_limits(trait):
    size_table = {
        'fob': {
            's': [0, 107],
            'm': [59, 221],
            'l': [59, 300]
        },
        'lea': {
            's': [0, 4],
            'm': [3, 6],
            'l': [6, 10]
        },
        'lbd': {
            's': [0, 4],
            'm': [3, 6],
            'l': [6, 10]
        },
        'rea': {
            's': [0, 4],
            'm': [3, 6],
            'l': [6, 10]
        },
        'rbd': {
            's': [0, 4],
            'm': [3, 6],
            'l': [6, 10]
        },
        'hnc': {
            's': [0, 8],
            'm': [5, 19],
            'l': [12, 23]
        },
        'vnc': {
            's': [0, 8],
            'm': [5, 18],
            'l': [12, 23]
        },
        'lcw': {
            's': [0, 4],
            'm': [2, 7],
            'l': [4, 10]
        },
        'rcw': {
            's': [0, 4],
            'm': [2, 7],
            'l': [4, 10]
        },
        'ma': {
            's': [0, 7],
            'm': [4, 14],
            'l': [8, 17]
        }
    }

    return size_table[trait]

# takes a trait and returnsa boolean stating wether or not the trait is a facial feature
def trait_is_relevant(trait):
    relevant_traits = ['fob', 'lea', 'lbd', 'rea', 'rbd', 'hnc', 'vnc', 'lcw', 'rcw', 'ma']

    if trait in relevant_traits:
        return True
    else:
        return False


def get_confidence(trait, value):
    size_limits = get_size_limits(trait)
    confidence = {}
    conf_s = 0
    conf_m = 0
    conf_l = 0

    if (value >= size_limits['s'][0]) or (value <= size_limits['s'][1]):
        s_p1 = [size_limits['s'][0], 1]
        s_p2 = [size_limits['s'][1], 0]
        conf_s = round(linear_function_modelling(s_p1, s_p2, value), 5)

   
    if (value >= size_limits['m'][0]) or (value <= size_limits['m'][1]):
        middle_ground = (size_limits['m'][0] + size_limits['m'][1]) / 2
        conf_m1 = 0
        conf_m2 = 0
        if value <= middle_ground:
            m1_p1 = [size_limits['m'][0], 0]
            m1_p2 = [middle_ground, 1]
            conf_m1 = round(linear_function_modelling(m1_p1, m1_p2, value), 5)
        else:
            m2_p1 = [middle_ground, 1]
            m2_p2 = [size_limits['m'][1], 0]
            conf_m2 = round(linear_function_modelling(m2_p1, m2_p2, value), 5)

        conf_m = conf_m1 if conf_m1 > conf_m2 else conf_m2

    if (value >= size_limits['l'][0]) or (value <= size_limits['l'][1]):
        l_p1 = [size_limits['l'][0], 0]
        l_p2 = [size_limits['l'][1], 1]
        conf_l = round(linear_function_modelling(l_p1, l_p2, value), 5)
    if conf_l > conf_m and conf_l > conf_s:
        confidence = {
            'value': conf_l,
            'size': 'l'
        }
    elif conf_m > conf_l and conf_m > conf_s:
        confidence = {
            'value': conf_m,
            'size': 'm'
        }
    elif conf_s > conf_l and conf_s >= conf_m:
        confidence = {
            'value': conf_s,
            'size': 's'
        } 

    if trait == 'lcw':
        print(confidence)
        print(value)
    return confidence


def linear_function_modelling(p1, p2, x):
    
    m = (p1[1] - p2[1]) / (p1[0] - p2[0])
    k = p1[1] - (p1[0] * m)
    y = m * x + k
    
    return y


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
            's': ['sorrow', 'neutral'],
            'm': ['sorrow', 'joy', 'disgust'],
            'l': ['joy']
        },
        'rcw': {
            's': ['sorrow', 'neutral'],
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
        size = size_object[trait]['size']
        emotions = table[trait][size]
        if emotions != []: 
            result[trait] = {
                'emotions': emotions,
                'value': size_object[trait]['value']
            }

    if result != {}:
        return(result)