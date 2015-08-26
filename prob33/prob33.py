from fractions import Fraction

pairs = [ (a,b) for a in range(1,10) for b in range(1,10) if a<b ]
special = []

for c in range(1,10):
	for a,b in pairs:
		if Fraction(int(str(c)+str(a)),int(str(c)+str(b)))==Fraction(a,b):
			special.append(Fraction(a,b))
		if Fraction(int(str(a)+str(c)),int(str(c)+str(b)))==Fraction(a,b):
			special.append(Fraction(a,b))
		if Fraction(int(str(c)+str(a)),int(str(b)+str(c)))==Fraction(a,b):
			special.append(Fraction(a,b))
		if Fraction(int(str(a)+str(c)),int(str(b)+str(c)))==Fraction(a,b):
			special.append(Fraction(a,b))

product = 1
for frac in special: product*=frac
print(product.denominator)
