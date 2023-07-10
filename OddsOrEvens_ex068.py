# CHALLENGE 068 ☻ Python Exercise 068: Write a program that plays Odds or Evens with the computer. The game will only
# interrupted when the player loses, showing the total number of consecutive wins he has achieved at the end of the game.

from random import randint

v = 0  # variable type counter for holding amount of times player won game
while True:
    player = int(input('Type a value: '))  # player (user) plays a number
    computer = randint(0, 11)  # computer choose a number between 1 and 10
    total = player + computer  # sum of player and computers values
    type = ' '  # variable that holds result (odd or even)
    while type not in 'OE':  # loop for getting Odds or Evens input + calculation of result based on numbers played
        type = str(input('Odds or Evens?[O/E]')).strip().upper()[0]
    print(f'You played {player} and the computer played {computer}. Total:{total}', end=' ')
    print(
        'Result is EVENS.' if total % 2 == 0 else 'Result is ODDS.')  # output based on dividing total by two returning the floating point value
    if type == 'E':
        if total % 2 == 0:
            print('You WON! :)')
            v += 1  # adds 1 everytime loop happens
        else:
            print('You lost...')
            break
    elif type == 'O':
        if total % 2 == 1:
            print('You WON! :)')
            v += 1
        else:
            print('You lost...')
            break  # flag for stopping game / while loop
    print('Lets play again. :D')
print(f'GAME OVER! You won {v} times.')
