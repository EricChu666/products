import os #operating system 
products = []

if os.path.isfile('Products_list.csv'):
	with open('Products_list.csv', 'r', encoding = 'utf-8') as f:
		for line in f:
			if 'name, price' in line:
				continue
			name, price = line.strip().split(',') #standard is ','
			products.append([name, price])
	for p in products:
		print('the product name is:', p[0], ',', 'the price is:', p[1])

else:
	ans = input('The file is not found. If you want to make a new list?')
	if ans == 'yes':
		while True:
			name = input('Please enter the name of the product:')
			if name == 'q':
				break
			price = input('Please enter the price of the product:')
			products.append([name, price])
		print('\n' + 'Your new product list is: ')
		for p in products:
			print('the price of', p[0], 'is:', p[1])
		with open('Products_list.csv', 'w', encoding = 'utf-8') as f:
			f.write('name, price\n')
			for p in products:
				f.write(p[0] + ',' + p[1] + '\n')
	elif ans == 'no':
		print('Okay, we will welcome next time.')
	else:
		print('Please type "yes" or "no."')
		raise SystemExit