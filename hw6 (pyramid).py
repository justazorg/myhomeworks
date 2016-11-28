wordic = input('enter your word:')
for index,_ in enumerate(wordic):
    print (" ".join(wordic[:index+1]))
