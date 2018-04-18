#Math Question
print('Welcome to the Random Multiplication Problem generator.')
from random import randint
#print(randint(10, 100))
a = randint(1, 50)
b = randint(1, 50)
print('If a = ' , a , "and b = " , b)
answer = input('What is a times b? ')
if(a*b == answer):
    print("\n Correct! Smartie Pants - have a candy! ")
else:
    print("\n Wrong!")
