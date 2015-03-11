def fmeasure(p, r):
	f = 2 * (p * r) / (p + r)
	print(f)

if __name__ == '__main__':
	p = 66.67
	r = 50.0
	fmeasure(p, r)