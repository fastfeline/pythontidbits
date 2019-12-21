#Multiplication to 13 in Python
print("Welcome to Collatz conjecture in Python")
print("Accepting an input - even numbers divide by 2; odd numbers triple and add 1")
base = input("What number shall I test?" )
base = int(base)
originalBase = int(base)
print(base)
#
while(base>1):
    if (base % 2) == 0:
        base = base/2
        print(base)
    else:
        base = base*3+1
        print(base)
if (base==1):
    print(originalBase, " has become 1!")
