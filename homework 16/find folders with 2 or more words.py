import os
import re
total_number = 0
for m in os.listdir("C:\\Users\\Никита\\Desktop\\homework 16\\papka"):
    if re.findall('\w+' ' ' '\w+', m):
                  total_number +=1
print("папок с двумя и более словами:", total_number)
for m in os.listdir("C:\\Users\\Никита\\Desktop\\homework 16\\papka"):
    s = re.findall('\w+' ' ' '\w+', m)
    for e in s:
        print(s)

