print("Hello world!")
f = open("dataset/emo_muster_2_1.csv", "r")
f.readline()
print(f.readline())

# main handles the entire flow of the program
# starts reading the file(s) -> could be outsourced later [REFACTORING]
# handles the numbers -> probabilities
# handles algorithm
# handles output

# "handles" means it calls the functions/ methods etc