def palidrome_check(element):
    element = element.lower()
    left = 0
    right = len(element) - 1
    
    while left < right:
        if element[left] != element[right]:
            return False
        left +=1
        right -+1
    return True

element = "Madamm" #racecar
check = palidrome_check(element)
if check:
    print("YES, Its Palidrome.")
else:
    print("NOT, Its Palidrome.")