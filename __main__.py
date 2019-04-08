import os
import data_conversion
from Evidence import Evidence
from DempsterRule import DempsterRule
# for missing feature: feature not in object -> no Evidence for it


# TODO: prompt for input file
# file_name = input('Please enter the file name: ')
file_name = 'C://Users//IBM_ADMIN//Documents//Uni//WBS//kbs-dempstersrule//dataset//emo_muster_2_1.csv'
# BASE_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'dataset', file_name)
# TODO: read input file
file = open(file_name)
# get traits featured in file
traits = file.readline().strip().split(';')

# TODO: create for loop for every line
# for line in file:
line = file.readline()
# TODO: data conversion
emotions = data_conversion.complete_conversion(traits, line.strip().split(';'))
# print(emotions)

# TODO: create Evidence for every feature and store in list, implement Evidence constructor
base_evidences = []
for feature in emotions:
    base_evidences.append(Evidence(emotions[feature]['emotions'], emotions[feature]['value']))

# TODO: accumulate by using helper variable ('final')
if len(base_evidences) < 2:
    raise ValueError('there are not enough features to do a proper anaylsis.')
final = DempsterRule(base_evidences[0], base_evidences[1]).get_output()
if len(base_evidences) > 2:
    for x in range(2, len(base_evidences)):
        final = DempsterRule(final, base_evidences[x]).get_output()

# TODO: final.get_plausability()
emotion_list = final.cal_plausibility()
belief_list = final.cal_belief()
print(emotion_list)
# print(belief_list)

    # TODO: get highest plausability = output
    # [TODO: belief]
    # TODO: write emotion and plausibility for frame into file/ output

