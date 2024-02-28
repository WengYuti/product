products = []
while True:
	name = input('請輸入商品名稱:')
	if name == 'q':
		break
	price = input('請輸入商品價格:')
	price = int(price) #存成整數
	products.append([name, price])
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
with open('products.csv', 'w', encoding='utf-8') as f: #指定編碼為UTF-8才不會有亂碼
	f.write('商品,價格\n')
	for p in products:
		f.write(p[0] + ',' + str(p[1]) + '\n')
#因為price已經是整數，所以這裡要再變回str字串才能用+
