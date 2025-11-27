line = input("Enter a Line of text: ")
line = line.lower()
words = line.split()
wc = {}
for word in words:
    wc[word] = wc.get(word, 0) + 1

print("\n word occurrences: ")
for word, count in wc.items():
      print(f"{word}: {count}")
      
