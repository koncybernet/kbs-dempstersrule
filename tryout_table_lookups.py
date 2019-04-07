import table_lookups

print("Hello world!")
f = open("dataset/emo_muster_2_1.csv", "r")
f.readline()
line = f.readline().strip().split(';')
print(line)

sizes = table_lookups.number_to_size(line)
print('sizes object:')
print(sizes)

emotions = table_lookups.size_to_emotion(sizes)
print('emotions object:')
print(emotions)