# DESAFIO 12 ☻
# Make an algorithm that reads the price of a product
# and displays its new price, with 5% discount.

# data collection
price = float(input('What is the price of the product?'))

# calculations
d = float(price * 5)
discount = float(d / 100)
newp = float(price - discount)

# output
print('The price for this product will be {:.2f} after 5% discount.'.format(newp))

