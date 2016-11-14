arr = []
word = input('latin word please:')
while word:
    arr.append(word)
    word = input('latin word please:')
for w in arr:
    if w.strip('\t') in w:
        print(w)
        
