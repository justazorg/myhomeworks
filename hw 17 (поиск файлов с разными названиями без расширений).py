import os 
count = 0
for root, dirs, files in os.walk('.'):
    for f in files:
        if f.split('.') not in names:
            count += 1
            names.append(f.split('.'))
print('Найдено {} файла(ов):'.format(count))

