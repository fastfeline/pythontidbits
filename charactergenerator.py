print("Hi! This is a D&D Character Generator")

#Race generator
print("What is your character's RACE?")
import random      #imports a thing: random number generator
for x in range(10): #range of 1 to 12
  raceint = random.randint(1,12)  #gets random number from 1 to 12
if(raceint == 1):
    print("Dwarf")
    race = "Dwarf"
elif(raceint == 2):
    print("Elf")
    race = "Elf"
elif(raceint == 3):
    print("Halfling")
    race = "Halfling"
elif(raceint == 4):
    print("Human")
    race = "Human"
elif(raceint == 5):
    print("Dragonborn")
    race = "Dragonborn"
elif(raceint == 6):
    print("Gnome")
    race = "Gnome"
elif(raceint == 7):
    print("Half-Elf")
    race = "Half-Elf"
elif(raceint == 8):
    print("Half-Orc")
    race = "Half-Orc"
elif(raceint == 9):
    print("Tiefling")
    race = "Tiefling"
else:
    fillblankrace = input("Choose your race:")
    print(fillblankrace)
    race = fillblankrace
print("Your character's race is " + race)

#Class generator
print("What is your character's CLASS?")
import random
for x in range(13):
  classint = random.randint(1,13)
if(classint == 1):
    print("Barbarian")
    dndclass = "Barbarian"
elif(classint == 2):
    print("Bard")
    dndclass = "Bard"
elif(classint == 3):
    print("Cleric")
    dndclass = "Cleric"
elif(classint == 4):
    print("Druid")
    dndclass = "Druid"
elif(classint == 5):
    print("Fighter")
    dndclass = "Fighter"
elif(classint == 6):
    print("Monk")
    dndclass = "Monk"
elif(classint == 7):
    print("Paladin")
    dndclass = "Paladin"
elif(classint == 8):
    print("Ranger")
    dndclass = "Ranger"
elif(classint == 9):
    print("Rogue")
    dndclass = "Rogue"
elif(classint == 10):
    print("Sorcerer")
    dndclass = "Sorcerer"
elif(classint == 11):
    print("Warlock")
    dndclass = "Warlock"
elif(classint == 12):
    print("Wizard")
    dndclass = "Wizard"
else:
    fillblankclass = input("Choose your class:")
    print(fillblankclass)
    dndclass = fillblankclass
print("Your character's class is " + dndclass)
