import numpy as np
import sys

coins = np.array([ 1, 2, 5, 10, 20, 50, 100, 200 ])

def num_poss(value, coin_list):
	if value>=1:
		return sum( num_poss(value-coin, coin_list[coin_list<=coin]) for coin in coin_list[coin_list<=value] )
	else: return 1

print(num_poss(int(sys.argv[1]), coins))
