print('最多輸入3次密碼')
i = 3
while i >0:
	password = input('請輸入密碼: ')

	if password == 'a123456':
		print('登入成功')
		break
	else:
		i = i-1
		if i ==0:
			print('密碼錯誤!')
			break
		else:
			print('密碼錯誤! 還有', i, '次機會')

	