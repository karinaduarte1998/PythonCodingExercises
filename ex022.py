# DESAFIO 022 ☻
# Crie um programa que leia o nome completo de uma pessoa e mostre:
# - O nome com todas as letras maiúsculas e minúsculas.
# - Quantas letras ao todo (sem considerar espaços).
# - Quantas letras tem o primeiro nome.

n = str(input('What is your full name?'))
print('Analyzing your name...')
print('Your name in capital letters {}'.format(n.upper()))
print('Your name in lower case {}'.format(n.lower()))
print('Your name has a total of {} letters'.format(len(n) - n.count(' ')))
print('Your first name has a total of {} letters'.format(n.find(' ')))




