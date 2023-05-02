import os

def read_file(filename):
	products = []
	with open(filename, 'r', encoding = 'utf-8') as f:
		for line in f:
			if 'name, price' in line:
				continue
			name, price = line.strip().split(',')
			products.append([name, price])
	for p in products:
		print('name:', p[0], ',', 'price:', p[1])
	return products

def user_input(products):
	while True:
		name = input('Please enter the name of the product: ')
		if name == 'q':
			break
		price = input('Please enter the price of the product: ')
		products.append([name, price])
	return products

def print_products(products):
	print('\nYour new product list is: ')
	for p in products:
		print('the price of', p[0], 'is:', p[1])

def write_file(filename, products):
	with open(filename, 'w', encoding = 'utf-8') as f:
		f.write('name, price\n')
		for p in products:
			f.write(p[0] + ',' + p[1] + '\n')

def main():
	filename = 'Products_list.csv'
	if os.path.isfile(filename):
		print('\nAccess succeeds! Welcome, your product list is:')
		products = read_file(filename)
		ans = input('\nDo you want to add more items? ')
		if ans == 'yes':
			items = user_input(products)
			print_products(items)
			write_file(filename, items)
		elif ans == 'no':
			print('Sure! If you have more items, please remember to write down in.')

	else:
		print('Cannot find the file!')
		ans = input('Do you want to make a list? ')
		if ans == 'yes':
			products = []
			products = user_input(products) #把使用者輸入的資料更新進products
			print_products(products)
			write_file(filename, products)
		elif ans == 'no':
			raise SystemExit
		else:
			print('Please type "yes" or "no."')

main()