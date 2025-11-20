def binary_search(data, target):             # data: a sorted list, target: the element you want to find
    low = 0 # starting index : 0
    high = len(data)
    print(low, high)
    while low <= high:   
        mid = (low + high) // 2
        print("mid:", mid, "value:", data[mid])         
        if data[mid] == target:
            print("if : ",data[mid])
            print("Target Found!")
            return mid
        elif data[mid] < target:
            low = mid+ 1
        else:
            high = mid- 1
    return -1
print("start Binary Searching...")
data = [3,22,34,22,66,7,55,4,6626,78,60,88,2]
print("Sorting data :",data)                       
data.sort()
target = int(input("Enter no : "))
result = binary_search(data, target)                 

if result != -1:
    print(f"Target Valie : {target} and its index is {result}.")
else:
    print(f"{target} not Found!")
