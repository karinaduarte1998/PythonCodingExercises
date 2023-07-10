# DESAFIO 036 ☻
# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da
# casa, o salário do comprador e em quantos anos ele vai pagar.
# A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

#print('Escolha seu idioma / Choose your language')
#lan = input('Digite PT para portugues / Type EN for english')
#if lan == 'PT':
#    print('Rodando programa em Portugues!')

casa = float(input('Qual o valor da casa?'))
salario = float(input('Qual o valor total do seu salario?'))
anos = float(input('Em quantos anos voce pretende pagar o emprestimo?'))

parcela = casa / (anos * 12)
pagamento = salario * 30 / 100
print('Para pagar uma casa de R${:.2f} reais em {} anos, as parcelas serao de R${:.2f} reais.'.format(casa, anos, parcela))
if parcela <= pagamento:
    print('O seu financiamento foi ACEITO!')
else:
    print('O seu financiamento foi NEGADO!')
