#Your code goes here


N = input("Enter : ")

seven = 0
sodd = 0
for no in N:
    if no.isdigit():
        no=int(no)
        if no % 2 == 0:
            seven+=no
        else:
            sodd+=no

print(seven)
print(sodd)




# li = [[ i*j for j in range(4)] for i in range(3)]
# print(li)
for j in range(3):
    for i in range(4):
        print(i*j)

print("1111111111111111")
# i = 0
# while i < 5:
#     if i == 2:
#         continue
#     else:
#         print(i,end = " ")   
#         i += 1

print("22222222222222222")
#Your code goes here

# n = int(input("Enter : "))
# s=0
# for i in range(1,n+1):
#     if i %2==0:
#         s +=i

# print(s)
print("3333333333333333")


s = 0
e = 100
w = 20


while s <= e:
    celsius = (5 / 9) * (s - 32)

    if celsius >=0:
        celsius = int(celsius)

    else:
        celsius = int(celsius) + 1

    # print(f"{s} {celsius}")
    print(s,celsius,sep = "\t") # sep for seperator

    s+=w


# for currentFahrenhietValue in range(s,e + 1,w):

#     celcius = int((currentFahrenhietValue - 32) * 5 /9)

#     print(currentFahrenhietValue,celcius,sep = "\t")