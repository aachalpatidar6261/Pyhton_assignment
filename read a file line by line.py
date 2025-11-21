file=open("datafile.txt","r")
lines=file.readlines()
#print(lines)

for line in lines:
    print(line)
file.close()