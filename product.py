products = []
while True:
	name = input('請輸入商品名稱:')
	if name == 'q':
		break
	price = input('請輸入商品價格:')
	#P= []
	#P.append(name)
	#p.append(price)
	#p = [name, price] 省了上面兩行
	products.append([name, price]) #省略上面4行
print(products)

for p in products:
	print(p[0], '$', p[1])
#字串可以做+及乘
#'abc' + '123' = 'abc123'
#'abc' * 3 = 'abcabcabc'

#open只是產生檔案，write才是真的寫入
#逗點在excel檔裡就是格子的區隔
#\n為換行
# with功能可以在你執行完後自動幫你close檔案，所以打開檔案需要執行的程式要寫在with裡面
with open('products.csv', 'w') as f:
	for p in products:
		f.write(p[0] + ',' + p[1] + '\n')
