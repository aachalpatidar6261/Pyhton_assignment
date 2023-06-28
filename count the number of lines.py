file = open("datafile.txt","r")
c =0
lines = file.readlines()
for line in lines:
    c +=1
print(c)
file.close()