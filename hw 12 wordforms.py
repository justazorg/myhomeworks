import re
regex = "(съе)(л|в?|сть?)(а?|и?|ш?)?(ий?|ая?|ие?)? "
f = open("your file here.txt", "r" ,encoding='utf-8')
j = re.findall(regex, f.read())
print(*j, sep = '\n')
