a= [11, 7, 1, 13, 21, 3, 7, 3]
b= [11, 3, 7, 1, 7]

# print("Yes", if is_subset(a, b) else "No")

def make_word():
  word = ""
  for ch in "spam":
    word +=ch
    yield word

print(list(make_word()))