# DESAFIO 065 ☻ Exercício Python 065: Crie um programa que leia vários números inteiros pelo teclado. No final da
# execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve
# perguntar ao usuário se ele quer ou não continuar a digitar valores.
ans = 'Y'
som = quant = med = maior = menor = 0
while ans in 'Yy':
    num = int(input('Type an integer number: '))
    som += num
    quant += 1
    if quant == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    ans = str(input('Do you wish to continue?')).upper().strip()[0]
med = som / quant
print(f'You typed {quant} numbers and the average sum between them is {med}')
print('The highest value was {} and the smallest value was {}'.format(maior, menor))
