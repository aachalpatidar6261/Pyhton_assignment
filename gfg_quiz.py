"""
class Solution:
    def nCr(self, n, r):
        # code here
        if r>n:
            return 0
        def fac(x):
            result = 1
            for i in range(2,x+1):
                result *= i
                
            return result
        
        return fac(n) // (fac(r) * fac(n-r))

# sol = Solution()
# n=3
# r=2
# print(sol.nCr(n,r))

# n = 1
# r=0
# print(sol.nCr(n,r))
print("-------------")

class Solution:
    def findDuplicates(self, arr):
        # code here
        dup = 0
        sec = []
        result = []
        for num in arr:
            if num in sec:
                result.append(num)
            else:
                sec.append(num)
        if result:
            return result
        else:
            return []
sol = Solution()
arr= [2, 3, 1, 8,6]
print(sol.findDuplicates(arr))


Given two arrays a[] and b[], your task is to determine whether b[] is a subset of a[].
class Solution:
    def isSubset(self, a, b):
        freq = {}
        
        # Count elements in a[]
        for val in a:
            if val in freq:
                freq[val] += 1
            else:
                freq[val] = 1

        # Check if each element in b[] is present in freq
        for val in b:
            if val in freq and freq[val] > 0:
                freq[val] -= 1
            else:
                return False  # Not found or already used up

        return True

a = [11, 7, 1, 13, 21, 3, 7, 3]
b = [11, 3, 7, 1, 7]
s = Solution()
print(s.issub(a,b))

Write a solution to delete all duplicate emails, keeping only one unique email with the smallest id.
# Write your MySQL query statement below
Delete from Person
where id not in (
    select id from (
    select Min(id) as id
    from Person
    group by email
    ) as temp
);

Write a solution to find employees who have the highest salary in each of the departments.
# Write your MySQL query statement below
select 
d.name as department,
e.name as employee,
e.salary as salary
from employee e
join department d
on
e.departmentId = d.id
where 
(e.salary, e.departmentID) in 
(select Max(salary), departmentID from employee
group by departmentId
);

Find all numbers that appear at least three times consecutively.
Return the result table in any order.
"""
n = [1,2,3,4,5]
result = list(map(lambda x : x*2,n))
print("MAP : ",result)

result = list(filter(lambda x : x%2==0, n))
print("Filter : ",result)

students = {'Alice': 85, 'Bob': 65, 'Charlie': 90}

filtered = dict(filter(lambda item: item[1] > 75, students.items()))
print(filtered)  # Output: {'Alice': 85, 'Charlie': 90}

students = {'Alice': 85, 'Bob': 85, 'Charlie': 90}

updated = dict(map(lambda item: (item[0], item[1] + 5), students.items()))
print(updated)  # Output: {'Alice': 90, 'Bob': 70, 'Charlie': 95}
sorted_students = sorted(students.items(), key=lambda item: item[1], reverse=True)

# Convert back to dict (optional)
sorted_dict = dict(sorted_students)
print(sorted_dict)