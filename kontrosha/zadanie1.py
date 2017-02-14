counter = 0
f = open('C:\\Users\\Никита\\Desktop\\kontrosha\\kontrol.txt').read()
for lines in f.split():
    if '</teiHeader>' not in lines:
        counter += 1
    else:
        break
print(counter)
with open('C:\\Users\\Никита\\Desktop\\kontrosha\\resultat.txt', 'w', encoding='utf-8') as file:
    print(counter, file=file)
print('результат распечатан в файл')


