# 6*(9!)<10**6 a proto cisla budou mit max 5 cifer ( 5*(9!)>10**5 ... peticiferna tedy cisla byt mohou )

from math import factorial
import timeit

curious = []

f = [ factorial(n) for n in range(0,10) ] # mnohem rychlejsi, nez ho pocitat

for n in range(3,10**6):
	num_list = [ int(num) for num in str(n) ]
	if sum( f[num] for num in num_list )==n:
		curious.append(n)

print curious
print sum(curious)
