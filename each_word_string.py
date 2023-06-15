#Write a Python program to count the occurrences of each word in a given sentence

def each_word(str):
    d = dict()
    word = str.split()

    for i in word:
        if i in d :
            d[i]+=1
        else:
            d[i] = 1
    return d


print(each_word("the sun is yellow and the moon is white"))