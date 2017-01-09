import random

def noun():
    nouns = ['собака','велосипед','коробка','радуга','телефон','тетрадь','хлеб','пирог','замок','билет','бритва','скамейка','магазин','колесо','щкафчик','тарелка']
    return random.choice(nouns)
def adverb():
    nouns = ['жарко','холодно','больно','страшно','громко','вызывающе','немедленно','быстро','яростно','высоко','далеко','мужественно','скучно']
    return random.choice(nouns)
def verb():
    nouns = ['горит','лежит','бежит','едет','прыгает','кушает','поет','разминается','опаздывает','тонет','сидит','идет','кидает','включает','пишет','дерется']
    return random.choice(nouns)
def sub_conj():
    nouns = ['потому что','если','пока','когда','так что','ибо']
    return random.choice(nouns)
def comp_conj():
    nouns = ['и','также','а','но','однако','зато']
    return random.choice(nouns)
def random_sentence():
    sentence = noun() + ' ' + verb() + ' ' + adverb() + ' ' + (sub_conj() or comp_conj()) + ' ' + noun() + ' ' + verb() + ' ' + adverb() + '.'
    return sentence
num_of_sents = random.randint(6, 20)
for i in range(num_of_sents):
    sentence = random_sentence()
    sentence = sentence.capitalize()
    print(sentence, end='  ')

    
