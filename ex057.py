# DESAFIO 057 ☻
''' Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'.
Caso esteja errado, peça a digitação novamente até ter um valor correto. '''
gender = 'M' == 'F'
while gender != 'M' and gender != 'F':
    gender = str(input('What is your gender? [M/F]')).upper().strip()[0]
print(f'Gender {gender} successfully registered!')

'''while gender not in 'MmFf':
    gender = str(input('Dados inválidos')'''
