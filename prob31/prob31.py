def num_poss(value):
	if value>=1:
		if value>=2:
			if value>=5:
				if value>=10:
					if value>=20:
						if value>=50:
							if value>=100:
								return num_poss(value-100)+num_poss(value-50)+num_poss(value-20)+num_poss(value-10)+num_poss(value-5)+num_poss(value-2)+num_poss(value-1)
							else:
								return num_poss(value-50)+num_poss(value-20)+num_poss(value-10)+num_poss(value-5)+num_poss(value-2)+num_poss(value-1)
						else:
							return num_poss(value-20)+num_poss(value-10)+num_poss(value-5)+num_poss(value-2)+num_poss(value-1)
					else:
						return num_poss(value-10)+num_poss(value-5)+num_poss(value-2)+num_poss(value-1)
				else:
					return num_poss(value-5)+num_poss(value-2)+num_poss(value-1)
			else:
				return num_poss(value-2)+num_poss(value-1)
		else:
			return num_poss(value-1)
	else:
		return 1

print num_poss(5)
