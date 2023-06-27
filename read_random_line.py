import random

file = open("file.txt","w")
file.write("this is python file\ni am Aachal Patidar \ni am current working in python programming language")
file.close()

file=open("file.txt", "r")
f = file.read().splitlines()
r = random.choice(f)
print("read a random line from a file > ",r)
file.close()
