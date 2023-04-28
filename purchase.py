products = []
while True: 
	name = input('Please enter the name of the product:')
	if name == 'q':
		break
	price = input('Please enter the price of the product:')
	products.append([name, price])

print(products)