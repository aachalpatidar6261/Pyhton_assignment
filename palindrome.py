def palindrome(string):
    left = 0
    rt = len(string)-1

    while rt >=left:
        if not string[left]==string[rt]:
            return False
        left+=1
        rt -=1
    return True
string = input("enter string : ")
print(palindrome(string))