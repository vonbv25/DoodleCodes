from math import *

def mysqrt(x):
	s = 1.
	kmax = 100
	tol = 1.e-14
	for k in range(kmax):
		print "before iteration %s, s= %s20.15f" % (k,s)
		s0 = s
		s = 0.5 * (s + x/s)
		delta_s = s- s0
		if abs(delta_s / x ) < tol:
			break
	print "after %s iterations, s = %20.15f" % (k,s)




