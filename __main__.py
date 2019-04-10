import os
import data_conversion
import util
from BasisMeasure import BasisMeasure
from DempsterRule import DempsterRule


# promt for input file
file_path = input('Please enter the absolute path of the file: ')
file = open(file_path)
# get traits featured in file
traits = file.readline().strip().split(';')

output = []
# loop through every row
for ind, line in enumerate(file):
    # data conversion
    emotions = data_conversion.data_cleansing(traits, line.strip().split(';'))

    # create Evidence for every feature and store in list
    base_bms = []
    for feature in emotions:
        base_bms.append(BasisMeasure(emotions[feature]['emotions'], emotions[feature]['value']))

    # accumulate basis measures
    if len(base_bms) < 2:
        raise ValueError('there are not enough features to do a proper anaylsis.')
    final = DempsterRule(base_bms[0], base_bms[1]).get_output()
    if len(base_bms) > 2:
        for x in range(2, len(base_bms)):
            final = DempsterRule(final, base_bms[x]).get_output()

    # calculate plausability and belief for final accumulated basis measure
    emotion_list = final.cal_plausibility()
    belief_list = final.cal_belief()

    # construct output
    current_high = [0, '']
    for emotion, plausibility in emotion_list:
        if plausibility > current_high[0]:
            current_high = [plausibility, emotion]
    output.append({
        'emotion': current_high[1],
        'plausibility': round(current_high[0], 2),
        'belief': util.get_belief_from_list(current_high[1], belief_list)
    })

# write output to file
f = open('output.txt', 'w+')
f.write('')
f = open('output.txt', 'a+')
for ind, i in enumerate(output):
    f.write('Frame #' + str(ind + 1))
    f.write(' ' + str(i))
    f.write('\n')
    print('Frame #' + str(ind + 1))
    print(i)
    print('\n')
