def Linear_search(data, target):
    print(f"Searching for {target} in this list...")
    for element in range(len(data)):
        print(f"checking item in index {element} : {data[element]}")
        if data[element] == target:
            print("Target Found!")
            return element
    return -1

data = [3,22,5,34,22,66,7,55,4,6626,78,60,88,2]
target = 66
result = Linear_search(data, target)
if result != -1:
    print(f"Target value {target} in the index {result}.")
else:
    print(f"{target} is not found in list.")