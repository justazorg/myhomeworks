import re

def open_html(f):
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    return content
content = open_html(r'C:\Users\Никита\Desktop\hw15 cats and dinos\dinos.html')
m = re.sub('динозавр', 'кот', content, flags= re.M)
p = re.sub('Динозавр', 'Кот', m, flags= re.M)
print(p)
with open('result.txt', 'w', encoding='utf-8') as file:
    print(p, file=file)
print('результат распечатан в файл')
