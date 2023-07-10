# DESAFIO 028 ☻
# Write a game-like program that makes the computer "think" of a number (whole)
# between 0 and 5 and asks the user to guess what number was chosen by the computer.
# The program must write on the screen if the user won or lost.

from random import randint
from time import sleep

print('*-*-* ' * 15)
str(input('Would you like to play a game?'))
print('I am going to think of a number between 1 and 5')
sleep(1.5)
#else: print('Whatever, see u next time')
print('Thinking of a number...')# Make computer think of a number
sleep(1.5)
computer = randint(1, 5)
n = int(input('What number did I think of?'))  # Player tries to guess the number
sleep(1.5)
print('WINNER! well done mf- you guessed right! Number {} ☻'.format(computer) if n == computer
      else 'Wrong one, I though number {} not {}. You lose mate.'.format(computer, n))
