# DESAFIO 045 ☻
# Crie um programa que faça o computador jogar Jokenpô com você.
from time import sleep
from random import randint
itens = ('Pedra', 'Papel', 'Tesoura')
print('\033[34;107mSuas opções:')
print('''[1] PEDRA 
[2] PAPEL 
[3] TESOURA''')
jogador = int(input('Qual é a sua jogada?'))
computer = randint(0, 2)
print('JO')
sleep(0.8)
print('KEN')
sleep(0.8)
print('PÔ!!!')
print('Você jogou: \033[1m {} \033[0;34;107m'.format(itens[jogador]))
print('O computador jogou: \033[1m {} \033[0m'.format(itens[computer]))
if jogador == 0 and computer == 0:
    print('\033[34;107m{:=^40}'.format('\033[1;35mEmpate!\033[34;107m'))
elif jogador == 0 and computer == 1:
    print('\033[0;34;107m{:=^40}'.format('\033[1;35mPapel cobre pedra. Você perdeu.\033[34;107m'))
elif jogador == 0 and computer == 2:
    print('\033[0;34;107m{:=^40}'.format('\033[1;35mPedra quebra tesoura. Você venceu.\033[34;107m'))
elif jogador == 1 and computer == 0:
    print('\033[0;34;107m{:=^40}'.format('\033[1;35mPapel cobre pedra. Você venceu.\033[34;107m'))
elif jogador == 1 and computer == 1:
    print('\033[0;34;107m{:=^40}'.format('\033[1;35mEmpate!\033[34;107m'))
elif jogador == 1 and computer == 2:
    print('\033[0;34;107m{:=^40}'.format('\033[1;35mTesoura corta papel. Você perdeu.\033[34;107m'))
elif jogador == 2 and computer == 0:
    print('\033[0;34;107m{:=^40}'.format('\033[1;35mPedra quebra tesoura. Você perdeu.\033[34;107m'))
elif jogador == 2 and computer == 1:
    print('\033[0;34;107m{:=^40}'.format('\033[1;35mTesoura corta papel. Você venceu!\033[34;107m'))
elif jogador == 2 and computer == 2:
    print('\033[0;34;107m{:=^40}'.format('\033[1;35mEmpate!\0330;34;107m'))
else:
    print('uhh')
    print('Jogada inválida')

