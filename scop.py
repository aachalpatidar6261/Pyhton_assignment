def findsum(a,b,*args): 
    sm = 1
    for i in args:
        sm *= i
    return sm
 
#Driver's code
z = findsum(1,2,3,4,5) # *args is 3,4,5 
# In the above code snippet the first two values will be store in the a and b rest of them will be store in *args.
print(z)


x = 10 
def foo(): 
    x +=1
    print("Value of x: ", x) 
foo()
print("outer : ",x)

# if we try to change the global variable valur insite the function(local) python interpriter gave error.