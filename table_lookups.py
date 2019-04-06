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

