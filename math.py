#Math Question
print('Welcome to the Random Math Problem generator.')
from random import randint
#print(randint(10, 100))
a = randint(1, 100)
b = randint(1, 100)
print('If a = ' , a , "and b = " , b)
answer = input('What is a+b? ')
if(a+b == answer):
    print("\n Correct! Smartie Pants - have a candy! ")
else:
    print("\n Wrong!")
