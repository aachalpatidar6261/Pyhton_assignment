# #Your code goes here

# N = input()

# seven = 0
# sodd = 0
# for no in N:
#     if no.isdigit():
#         no=int(no)
#         if no%2 == 0:
#             seven+=no
#         else:
#             sodd+=no

# print(seven)
# print(sodd)

#Your code goes here
N = int(input())
fac = 1
while N>0:
    fac *= N
    N-=1
print("fac : ",fac)
