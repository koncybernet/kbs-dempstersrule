import data_conversion

print("Hello world!")
f = open("dataset/emo_muster_2_1.csv", "r")
f.readline()
line = f.readline().strip().split(';')
print(line)

sizes = data_conversion.number_to_size(line)
print('sizes object:')
print(sizes)

emotions = data_conversion.size_to_emotion(sizes)
print('emotions object:')
print(emotions)