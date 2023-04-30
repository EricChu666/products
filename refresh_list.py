#read the file
products = []

with open('Products_list.csv', 'r', encoding = 'utf-8') as f:
	for line in f:
		if 'name, price' in line:
			continue
		name, price = line.strip().split(',') #standard is ','
		products.append([name, price])
print(products)