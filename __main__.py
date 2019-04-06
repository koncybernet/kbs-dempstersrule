from Evidence import BasisMeasure

# print("Hello world!")
# f = open("dataset/emo_muster_2_1.csv", "r")
# f.readline()
# print(f.readline())

# kriegen die daten aus csv - done

# test = {'fob': 29930, 'lea': 24, 'lbd': 22, 'rea':22, 'rbd': 21, 'hnc': 5, 'vnc': 3, 'lcw': 10, 'rcw': 10, 'ma': 84}
input = {'stirnfalten': 's', 'augenoeffnung': 'm', 'brauenabstand': 'm', 'nasenfalten': 's', 'wangenfalten': 's'}

list = []

list.append(BasisMeasure('stirnfalten', input['stirnfalten']))
list.append(BasisMeasure('augenoeffnung', input['augenoeffnung']))
list.append(BasisMeasure('brauenabstand', input['brauenabstand']))
list.append(BasisMeasure('nasenfalten', input['nasenfalten']))
list.append(BasisMeasure('wangenfalten', input['wangenfalten']))

print(list)

# TODO: beispielobject konstruieren, inhalt ist emotion
# TODO get possible emotions and construct list
# TODO: akkumulieren
# TODO: dingsi berechnen



# main handles the entire flow of the program
# starts reading the file(s) -> could be outsourced later [REFACTORING]
# handles the numbers -> probabilities
# handles algorithm
# handles output

# "handles" means it calls the functions/ methods etc