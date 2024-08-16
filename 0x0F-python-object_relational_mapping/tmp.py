#!/usr/bin/python3

myvar = '*&$#@my 820 text'
myvar2 = ''

for char in myvar:
    if char == ' ' or char.isalnum():
        print(char, end='')
        myvar2 += char
    
print()