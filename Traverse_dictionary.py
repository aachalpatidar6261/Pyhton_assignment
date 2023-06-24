ball = {"red" : 10,"black":20,"green":30,"yellow" : 40}
# built-in function of dictionary
keys = ball.keys()
print("keys of ball :",keys)
value = ball.values()
print("\nvalue of ball :",value)
item = ball.items()
print("\nitem in ball :",item)

# without using built-in function
print("\nkeys in the ball-\n")
for i in ball:
    print(i)

print("\nvalue in ball - \n")
for i in ball:
    print(ball[i])

print("\ncolor : quantity of ball-\n")
for i in ball:
    print(i , " : ",ball[i])