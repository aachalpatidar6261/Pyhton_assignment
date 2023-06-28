# file=open("datafile.txt","a")
# file.write("\n We took the value of N from the user (dynamic Input) \n then gave our program a text file containing some random content \n  and then opened it in reading mode. \n")
# file.close()

file = open("datafile.txt","r")
lines = file.readlines()

for line in lines[-4:]:  # blank line are also account as a line
    print(line)
file.close()