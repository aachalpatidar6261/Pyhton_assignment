from collections import Counter

dic = {'a':44,'b':67,'c':54,'f':90,'s':40,'n':100,'t':120}
k = Counter(dic)
print(k)

high = k.most_common(3)
for i in high:
    print(i[0]," : ",i[1])

