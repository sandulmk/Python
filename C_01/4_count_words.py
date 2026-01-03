line=input("Enter a line of text")
words=line.split()
word_count={}
for word in words:
    word_count[word]=word_count.get(word,0)+1
print(word_count)
