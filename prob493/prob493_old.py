from scipy.misc import comb
import numpy as np
from math import factorial

# 20 vytazenych micku, mezi ne dam n-1 prihradek a tim jim dam barvy
# n je pocet barev
# pak se musim zbavit vsech moznosti, ktere uvazuji vice nez 10 micku v prihradce
def colorcount(n):
	if n>1:
		return comb(7,n,exact=True)*(comb(19,n-1,exact=True)-n*sum(comb(i,n-2,exact=True) for i in range(0,9)))
#	elif n==2:
#		return comb(7,n,exact=True)
	else:
		return 0
#	return 10**n*(comb(7,n,exact=True)*comb(9*n,20-n, exact=True))/total_poss

counts = np.array([ colorcount(n) for n in range(1,8) ])
print counts
probs = counts/float(sum(counts))
print probs
print '{0:.19f}'.format(sum(probs*np.arange(1,8,1)))

from itertools import combinations

def var(n,k):
	if k>1: return n*var(n-1,k-1)
	else: return n-k+1

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
print counts2
probs = counts2/float(sum(counts2))
print probs
print '{0:.9f}'.format(sum(probs*np.arange(1,8,1)))

#for n in range(2,8): print n,colorcount_prob(n)
#print sum( n*colorcount_prob(n) for n in range(2,8) )

#from itertools import combinations
#import numpy as np
#
#offset = lambda j: np.array([ 10*j for i in range(0,10) ])
#
#def count_colors(turn):
#	colors = set(range(0,7))
#	for j in colors:
#		for i in offset(j)+np.arange(0,10,1):
#			if i in turn:
#				colors = colors-set([j])
#	print len(colors)
#	return 7-len(colors)
#
#expected = sum(count_colors(turn) for turn in combinations(range(0,70),20))/len(combinations(range(0,70),20))
#
#print expected
