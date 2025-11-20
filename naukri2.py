# Given an integer ‘N’, your task is to write a program that returns all the divisors of ‘N’ in ascending order.
# For example:
# 'N' = 5.
# The divisors of 5 are 1, 5.

gen = (i for i in range(5))
reversed_list = reversed(list(gen))
print("reversed_list : ",reversed_list)

def printdivisors(N):
    divisior = []
    for i in range(1, int(N**0.5)+1):
        if N % i == 0:
            divisior.append(i)
            if i != N // 1:
                divisior.append(N//i)
    return sorted(divisior)
            

N = 10
print("Divisors: ",printdivisors(N))

#########3 both work same , first by chatgpt and second by code360

from typing import List

def printDivisors(n: int) -> List[int]:
    ans = []

    # Traversing from 1 to 'N'.
    for i in range(1, n + 1):
        if n % i == 0:
            ans.append(i)

    return ans