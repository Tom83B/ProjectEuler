def pandigital(a,b,c):
	if c>10000: return False
	else:
		if len(set(str(a)+str(b)+str(c))-set(['0'])) == 9:
			return True
		else: return False

print(set([ a*b for a in range(1,100) for b in range(100,10000) if pandigital(a,b,a*b) ]))
print(sum(set([ a*b for a in range(1,100) for b in range(100,10000) if pandigital(a,b,a*b) ])))
