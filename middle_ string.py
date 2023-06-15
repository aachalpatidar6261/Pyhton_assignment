def fun(str1,str2):

    length=len(str1)//2

    st1=str1[:length]
    st2=str1[length:]

    complate_string=st1+" "+str2+" "+st2
    print(complate_string)

s1=input("Enter String: ")
s2=input("Enter string that is add middle of the string: ")
fun(s1,s2)
