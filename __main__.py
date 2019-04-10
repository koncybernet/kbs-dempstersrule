import os
import data_conversion
import util
from BasisMeasure import BasisMeasure
from DempsterRule import DempsterRule


# TODO: prompt for input file
file_name = input('Please enter the file name: ')
# file_name = 'C://Users//casch//Documents//Uni//WBS//kbs-dempstersrule//dataset//emo_muster_2_3.csv'
BASE_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'dataset', file_name)
# TODO: read input file
file = open(BASE_PATH)
# get traits featured in file
traits = file.readline().strip().split(';')

output = []
# TODO: create for loop for every line
for ind, line in enumerate(file):
    # line = file.readline()
    # TODO: data conversion
    emotions = data_conversion.complete_conversion(traits, line.strip().split(';'))
    # print(emotions)

    # TODO: create Evidence for every feature and store in list, implement Evidence constructor
    base_bms = []
    for feature in emotions:
        base_bms.append(BasisMeasure(emotions[feature]['emotions'], emotions[feature]['value']))

    # TODO: accumulate by using helper variable ('final')
    if len(base_bms) < 2:
        raise ValueError('there are not enough features to do a proper anaylsis.')
    final = DempsterRule(base_bms[0], base_bms[1]).get_output()
    if len(base_bms) > 2:
        for x in range(2, len(base_bms)):
            final = DempsterRule(final, base_bms[x]).get_output()

    # TODO: final.get_plausability()
    emotion_list = final.cal_plausibility()
    belief_list = final.cal_belief()

    current_high = [0, '']
    for emotion, plausibility in emotion_list:
        # print(plausibility)
        if plausibility > current_high[0]:
            current_high = [plausibility, emotion]

    output.append({
        'emotion': current_high[1],
        'plausibility': current_high[0],
        'belief': util.get_belief_from_list(current_high[1], belief_list)
    })


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
