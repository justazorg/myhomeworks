file = open("your txt file here","r",encoding='utf8')
arriva = 0
arr = 0
for word in file.read().split():
    if len(word) >= 0:
        arriva += 1
    if len(word) >= 10:
        arr += 1
print(arr/arriva*100)        
file.close()
        
