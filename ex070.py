# DESAFIO 070 ☻ Python Exercise 070:
# Create a program that reads the name and price of several products.
# The program should ask whether the user is going to continue or not. At the end, show:
# A) What is the total amount spent on the purchase.
# B) how many products cost more than R$1000.
# C) what is the name of the cheapest product.
total = over_thousand = menor = cont = 0
cheap = ''
while True:
    print('Welcome to KD store')
    product = str(input('Product name:'))
    price = float(input('Price R$:'))
    cont += 1
    total += price
    if price > 1000:
        over_thousand += 1
    if cont == 1 or price < minor:
        minor = price
        cheap = product
    ans = ' '

    ans = str(input('Would you like to register another product?[Y/N]')).strip().upper()[0]
    if ans != 'N':
        continue
    break
print('{:-^40}'.format(' End of program '))
print(f' Costumer bought {over_thousand} product(s) that costs over a thousand.')
print(f' The cheapest product was {cheap} and costed R${minor:.2f}')
print(f' R${total:.2f} spent in total.')

