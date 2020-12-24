def seek_string(string):
	i = 0

	count = 1

	while True:
		s = ''
		if i < len(string):
			x = string[i]

			if x != " ":
				x = count
				count += 1
			else:
				count = 0
				x = count
				count += 1	

			if x == 0:
				x = " "
				s += x
			else:
				s += str(x)
			print(s, end="")

		i += 1

seek_string("Ahmed Mohamed ali hossame ibrahim abdelrahman")