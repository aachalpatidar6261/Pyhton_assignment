file = open("datafile.txt","w")
file.write("One incorrect definition for conjuncture \n anecdotes, seamed and charred into process \n To reshape our form, towards another incomplete \nHope changes the outcome of language")

file.close()
print("datafile is created..!")

file=open("datafile.txt","r")
print(file.read())
file.close()
print("data is read..!")

file = open("datafile.txt","a")
file.write("\n \nThis is written by Aachal Patidar.....!! \n")
file.close()
print("data is written successfukly !!")

file=open("datafile.txt","r")
print(file.read())
file.close()