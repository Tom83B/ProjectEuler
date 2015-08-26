doublepals = []

for n in range(1,1000000):
	rev = int(str(n)[::-1])
	binary_str = "{0:b}".format(n)
	if str(n)==str(rev) and binary_str==binary_str[::-1]:
		doublepals.append(n)

print(sum(doublepals))
