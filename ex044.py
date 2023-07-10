# DESAFIO 044 ☻
# Elabore um programa que calcule o valor a ser pago por um produto,
# considerando o seu preço normal e condição de pagamento:
# - à vista dinheiro/cheque: 10% de desconto;
# - à vista no cartão: 5% de desconto;
# - em até 2x no cartão: preço formal;
# - 3x ou mais no cartão: 20% de juros.
print('{:=^40}'.format('Lojinha da Ka'))
preco = float(input('Qual o preço do produto?'))
print('''E qual será a forma de pagamento?
    [1] à vista no dinheiro/pix 
    [2] à vista no cartão de débito
    [3] em até 2x no cartão de crédito
    [4] em 3x ou mais vezes no cartão de crédito''')
opcao = float(input('Digite o número da opção desejada:'))
if opcao == 1:
    total = preco - (preco * 10 / 100)
    print('Para pagamentos à vista no dinheiro ou PIX, é concedido um desconto de 10%. \nAssim, sua compra no valor de '
          'R${:.2f} sairá por {:.2f}.'.format(preco, total))
elif opcao == 2:
    total = preco - (preco * 5 / 100)
    print('Para pagamentos à vista no cartão, é concedido um desconto de 5%. \n Assim, sua compra no valor de '
          'R${:.2f} sairá por R${:.2f}reais.'.format(preco, total))
elif opcao == 3:
    parcela = preco / 2
    print('Sua compra será parcelada em 2x sem juros.')
    print(' As parcelas vão sair no valor de R${'
          ':.2f}reais, e o valor total será de R${:.2f}reais.'.format(parcela, preco))
elif opcao == 4:
    parcelas = int(input('Em quantas parcelas você deseja realizar o pagamento?'))
    total = preco + (preco * 20 / 100)
    parcela = total / parcelas
    print('Sua compra será parcelada em {}x vezes com juros.'.format(parcelas))
    print('Assim, as parcelas no valor de R${:.2f} reais no cartão de crédito, \nvão totalizar o valor de R${:.2f}reais'.format(parcela, total))
else:
    print('Opção inválida!')

