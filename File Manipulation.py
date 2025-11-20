def word_count(filename):
    counts = {}

    with open(filename, "r") as file:
        for line in file:
            words = line.lower().split()  #list of words
            for word in words:
                word = word.strip(".,?!()[]{}\"'")  ## remove punctuation
                if word:
                    counts[word] = counts.get(word, 0) + 1
    
    for word in sorted(counts):
        print(f"{word} : {counts[word]}")

filename = "text_file.txt"
word_count(filename)
