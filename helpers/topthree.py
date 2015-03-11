# select top three

def topThree(d):

	f  = ''
	s  = ''
	t  = '' 
	fc = 0
	sc = 0
	tc = 0
	for k in d:
	    if d[k] > fc:
	        fc = d[k]
	        f  = k
	    elif d[k] > sc:
	        sc = d[k]
	        s  = k
	    elif d[k] > tc:
	        tc = d[k]
	        t  = k

	return f, fc, s, sc, t, tc