print("Code", "Chef")
print(8)
print(13, end=" ")
print(21)
print("p","pr")
print("Hello", "World", 5, "endl", 2)
print("Hello")
print(" World!")
S ="I love CodeChef"
for i in S:
    if i == " ":
        print(i,end="")
n = 5
for i in range(n):
    print("*"*4)
class Solution(object):
    def mergeAlternately(self, word1, word2):
        result = []
        i=0
        j=0

        len1,len2 = len(word1), len(word2)

        while i<len1 and j<len2 : 
            result.append(word1[i])
            result.append(word2[j])
            i+=1
            j+=1

        result.extend(word1[i:])
        result.extend(word2[j:])

        return "".join(result)

Sol = Solution()
print(Sol.mergeAlternately("ab","pqrs"))

sentence = "IceCreAm"

for word in sentence:
    if word == "a" and word=="e" and word == "i" and word=="o" and word == "u" and word=="A" and word == "E" and word=="I" and word == "O" and word=="U":
        