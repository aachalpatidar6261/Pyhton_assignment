file = open("datafile.txt","r")
lines=file.readlines()
print(lines) # readlines split line in files, it is trit one line is one element of list.
n = 3
for line in lines[0:n]:
    print(line)
file.close()