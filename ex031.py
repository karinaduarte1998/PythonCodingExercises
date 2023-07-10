# DESAFIO 031 ☻
# Develop a program that asks the distance travelled on a trip in Km.
# Calculate the price of the ticket, charging R$0,50 per KM for travels of up to 200KM
# and R$0,45 for longer trips.

distance = float(input('In Km, what distance have you travelled?'))
ticket1 = distance * 0.50
ticket2 = distance * 0.45
if distance <= 200:
    print('The ticket will cost R${:.2f}.'.format(ticket1))
else:
    print('The ticket will cost R${:.2f}.'.format(ticket2))
# another way (shorter)
# distance = float(input('In Km, what distance have you travelled?'))
# price = distance * 0.5 if distance <= 200 else distance * 0.45
# print('The price for your ticket will be R${:.2f}.'.format(price))