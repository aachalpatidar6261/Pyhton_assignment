l = [(1,2,3),(),("a","b"),()]
print(l)

print("After removing empty tuple in list")
for i in l:
    if i==():
        l.remove(i)
print(l)
