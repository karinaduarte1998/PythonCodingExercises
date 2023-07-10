# DESAFIO 048 ☻
# Refaça o DESAFIO 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.
# Desafio 009: Make a program that reads any Whole Number and show in the screen its multiplication table.
n = int(input('\033[1;30;107mEscolha um número para ver a sua tabuada: '))
for c in range(1, 11):
    print('{} x {} = {}'.format(n, c, n*c))

