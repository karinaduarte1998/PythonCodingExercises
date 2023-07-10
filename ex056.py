# DESAFIO 056 ☻
# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
# No final do programa, mostre: a média de idade do grupo,
# qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.
media = 0
older = 0
eldest = ''
underfem = 0
for c in range(1, 5):
    name = input('What is your name?').strip().upper()
    age = int(input('How old are you?'))
    gender = input('M or F?').strip()
    media += age
    if c == 1 and gender in 'Mm':
        older = age
        eldest = name
    if gender in 'Mm' and age > older:
        older = age
        eldest = name
    if gender in 'Ff' and age < 20:
        underfem += 1
print(
    'O homem mais velho tem {} anos e o seu nome é: {}'.format(older, eldest))
print('A média de idade do grupo é de {:.2f}'.format(media/4))
print('Existem {} mulheres menores de 20 anos no grupo.'.format(underfem))
