from scipy.misc import comb
from itertools import combinations
import numpy as np

def ccount2(n):
	poss = []
	for tup in combinations(range(1,20),n-1):
		diff = np.diff(np.concatenate(([0], np.array(tup), [20])))
		# diff ma nyni pocet prvku=pocet barev, cislo urcuje pocet micku jedne barvy
		if len(diff[diff>10])==0:
			poss.append(diff)
	retvalue = 0
	for tup in poss:
		test = 1
		for a in tup:
			test *= comb(10,a)
		# potreba priradit vahy jednotlivym moznostem
		retvalue += test
	# vynasobit poctem moznosti, jak muzeme ze 7 barev vybrat n
	return comb(7,n)*retvalue

counts2 = np.array([ ccount2(n) for n in range(1,8) ])
probs = counts2/float(sum(counts2))
print '{0:.9f}'.format(sum(probs*np.arange(1,8,1)))
