products = []
while True:
	name = input('請輸入商品名稱:')
	if name == 'q':
		break
	price = input('請輸入商回價格:')
	#P= []
	#P.append(name)
	#p.append(price)
	#p = [name, price] 省了上面兩行
	products.append([name, price]) #省略上面4行
print(products)
