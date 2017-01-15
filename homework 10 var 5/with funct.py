def function(s):
    file = open(s, 'r', encoding='utf-8')
    words = [word for line in file for word in line.split()]
    return words
def count():
    adj = 0
    for line in (function("dzzz.txt")):
        for word in line.split():
            if word.endswith('ons'):
                adj += 1         
    return adj
def average():
    a = []
    for line in (function("dzzz.txt")):
        for word in line.split():
            if word.endswith('ons'):
                a.append(word)
    av = sum(len(word) for word in a)/len(a)
    return av
print('всего прилагательных с суффиксом "-ons":', count())
print('средняя длина:', average())
                
                
    
    

        
    

