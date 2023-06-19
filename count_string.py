l = ["aba","def","ghi","jkl","mno","pql"]
c = 0
for string in l:
    if len(string)>1 and string[0]==string[-1]:
        c +=1
print(c)