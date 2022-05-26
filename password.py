print('最多輸入3次密碼')
password = 'a123456'
i = 3
while True:

	pwd = input('請輸入密碼: ')
	i = i-1

	if pwd == password:
		print('登入成功')
		break
	else:
		if i == 0:
			print('密碼錯誤!')
			break
		else:
			print('還有', i, '次機會')

	