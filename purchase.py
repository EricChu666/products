products = []
while True: 
    name = input('Please enter the name of the product:')
    if name == 'q':
        break
    price = input('Please enter the price of the product:')
    products.append([name, price])

print(products)

for p in products:
    print('the price of', p[0], 'is:', p[1])

with open('Products_list.csv', 'w', encoding = 'utf-8') as f:
    f.write('name, price\n')
    for p in products:
        f.write(p[0] + ',' + p[1] + '\n')