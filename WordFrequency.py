def word_frequency(infile):
    word_count = {}

    file = open(infile, 'r')
    for line in file:
        words = line.lower().split()
        for word in words:  
            word_count[word] = word_count.get(word, 0) + 1
    file.close()

    return word_count

infile = 'sometext.txt'
word_freq = word_frequency(infile)

for word, count in word_freq.items():
    print(f"'{word}' appears {count} times")
