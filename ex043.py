# DESAFIO 042 ☻
# Desenvolva uma lógica que leia o peso e a altura de uma pessoa,
# calcule seu Índice de Massa Corporal (IMC) e mostre seu status,  de acordo com a tabela abaixo:
# - IMC abaixo de 18,5: Abaixo do Peso
# - Entre 18,5 e 25: Peso Ideal
# - 25 até 30: Sobrepeso
# - 30 até 40: Obesidade
# - Acima de 40: Obesidade Mórbida
peso = float(input('\033[33;107mQual é o seu peso em kilogramas?'))
altura = float(input('Qual é a sua altura em metros?'))
IMC = peso / (altura ** 2)
print('Seu IMC é de: \033[1m{:.1f}\033[0;33;107m'.format(IMC))
if IMC < 18.5:
    print('Você está \033[1;31mabaixo\033[0;33;107m do seu peso ideal.')
elif 18.5 <= IMC < 25:
    print('Você e stá no seu peso \033[1;36mideal.')
elif 25 < IMC <= 30:
    print('Você está na faixa de \033[1;31msobrepeso.')
elif 30 < IMC <= 40:
    print('Você está na faixa da \033[1;31mobesidade.')
else:
    print('Você está na faixa da \033[1;31mobesidade mórbida.')
