a = 0
i = 0

while i < 10:
	if a == 0:
		print "{0}".format(a)
		i = i + 1
		b = a + 1
		new = a + b
	print "{0}".format(new)
	i = i + 1
	b = a
	a = new
	new = a + b