def round(digits):
	convert_digit = str(digits)
	find_cvrt = convert_digit.find(".") # get index of dot
	ceil_or_floor = convert_digit[find_cvrt:] 
	float_num = float(ceil_or_floor)

	if float_num == 0 or float_num < 0.5:
		return int(digits)
	elif digits == int(digits):
		return int(digits)
	else:
		num = digits + 1
		return int(num)

print(round(1.231324))