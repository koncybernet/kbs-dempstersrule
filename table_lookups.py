def size_to_emotion():
    table = {
        'fob': {
            's': ['joy1', 'joy2', 'anger1', 'anger2', 'disgust1', 'disgust2', 'disdain1', 'disdain2'],
            'm': ['surprise', 'anger1', 'disgust1', 'disgust2', 'fear1', 'fear2', 'sorrow1', 'sorrow2', 'disdain1', 'disdain2'],
            'l': ['surprise', 'fear1', 'fear2', 'sorrow1', 'sorrow2']
        },
        'lea': {
            's': ['joy1', 'joy2', 'disgust1', 'disgust2', 'sorrow1', 'sorrow2', 'disdain2'],
            'm': ['joy1', 'joy2', 'anger1', 'anger2', 'disgust1', 'sorrow1', 'disdain1'],
            'l': ['surprise', 'anger1', 'anger2', 'fear1', 'fear2']
        },
        'lbd': {
            's': ['anger1', 'anger2', 'disgust2', 'sorrow1', 'sorrow2'],
            'm': ['joy1', 'joy2', 'disgust1', 'disgust2', 'sorrow1', 'disdain1', 'disdain2'],
            'l': ['surprise', 'fear1', 'fear2']
        },
        'rea': {
            's': ['joy1', 'joy2', 'disgust1', 'disgust2', 'sorrow1', 'sorrow2', 'disdain1'],
            'm': ['joy1', 'joy2', 'anger1', 'anger2', 'disgust1', 'sorrow1', 'disdain2'],
            'l': ['surprise', 'anger1', 'anger2', 'fear1', 'fear2']
        },
        'rbd': {
            's': ['anger1', 'anger2', 'disgust2', 'sorrow1', 'sorrow2'],
            'm': ['joy1', 'joy2', 'disgust1', 'disgust2', 'sorrow1', 'disdain1', 'disdain2'],
            'l': ['surprise', 'fear1', 'fear2']
        },
        'til': {
            's': ['joy1', 'joy2', 'surprise', 'anger1', 'anger2', 'disgust1', 'disgust2', 'fear1', 'fear2', 'sorrow1', 'sorrow2', 'disdain1', 'disdain2'],
            'm': ['disgust1', 'disgust2', 'disdain1', 'disdain2'],
            'l': []
        }
    }