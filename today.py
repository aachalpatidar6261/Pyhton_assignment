n = 5
for i in range(1,n+1):
    print("   "*(n-i)+" * "*(i-1)+" * "*i)
for i in range(1,n+1):
    print("   "*(i)+" * "*(n-i)+" * "*((n-1)-i))

for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end=" ") 
    print()

for i in range(1,n+1):
    print(str(i)*i)