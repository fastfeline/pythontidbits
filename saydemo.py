from os import system
system('say Hello. What is your name?')
name = input('Type your name here!     ')
system('say Hello,' + name)
system('say Type a Letter from A to F.')
grade = input('Type here(lowercase)     ')
system('say I got a  ' + grade + '  on my report card.')
system('say Goodbye!')
