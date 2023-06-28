file = open("datafile.txt","r")
lines = file.read()
#print(lines)
file.close()

file = open("file.txt","a")
file.write(lines)
file.close()

file = open("file.txt","r")
print(file.read())
file.close()
    