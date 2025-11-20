n = 5
for i in range(1,n+1):
    print("*"*i)

print("1-----+++----++++----+++----")
for i in range(1,n+1):
    print(" "*i+"*"*((n+1)-i))

print("2-----+++----++++----+++----")
for i in range(1,n+1):
    print(" "*(n-i)+"*"*i)
print("3-----+++----++++----+++----")
for i in range(1,n+1):
    print("*"*((n+1)-i)+" "*i)

print("4-----+++----++++----+++----")

for i in range(1,n+1):
    print("   "*(n-i)+" * "*(i-1)+" * "*i)
for i in range(1,n+1):
    print("   "*(i)+" * "*(n-i)+" * "*((n-1)-i))
print("5-----+++----++++----+++----")

for i in range(1,n+1):
    for j in range(1,i+1):
        print(j, end="")
    print()
print("6-----+++----++++----+++----")

for i in range(1, n+1):
    print(str(i)*i)