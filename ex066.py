# DESAFIO 066 ☻ Exercício Python 066: Crie um programa que leia números inteiros pelo teclado. O programa só vai
# parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram
# digitados e qual foi a soma entre elas (desconsiderando o flag).

soma = cont = 0
while True:
    n = int(input('Type a number (type 999 to stop):'))
    if n == 999:
        break
    cont += 1
    soma += n
print(f'You typed {cont} numbers')
print(f'The total sum of the values is: {soma}')
