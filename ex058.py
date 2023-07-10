# DESAFIO 058 ☻
"""Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10.
Só que agora o jogador vai tentar adivinhar até acertar,
mostrando no final quantos palpites foram necessários para vencer."""


from random import randint
from time import sleep
print('*-*-*' * 15)
str(input('Would you like to play a game?'))
print('*-*-*' * 15)
str(input('I am going to think of a number between 1 and 10, if you guess what number it is, you win.☻'))

sleep(0.5)
print('Thinking of a number...')

sleep(1)
c = 0
number = randint(0, 10)
guess = int(input('What number did I think of?'))
print('*-*-*' * 15)
while guess != number:
    guess = int(input('That is not the number I though of, try again.'))
    c += 1
    if guess == number:
        break
print('*-*-*' * 15)
print(f'You guessed correctly! I though of number {number}')
if c == 0:
    print('WINNER~! You guessed first time round!! ☻')
else:
    print(f'You needed {c+1} chances to guess the number correctly!')
print('*-*-*' * 15)

