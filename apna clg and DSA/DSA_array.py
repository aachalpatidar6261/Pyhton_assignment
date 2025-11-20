# MAX
arr = [56,87,99,658,20,6,999,978,44]
max = arr[0]
for num in arr:
    if max < num:
        max = num
print("Max in Array : ", max)

# MIN
min = arr[0]
for num in arr:
    if min > num:
        min = num
print("Min in array : ",min)
