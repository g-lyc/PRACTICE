import random
import cProfile

def f1(In):
	l1 = sorted(In)
	l2 = [i for i in l1 if i<0.5]
	return [i*i for i in l2]
	
def f2(In):
	l1 = [i for i in In if i<0.5]
	l2 = sorted(l1)
	return [i*i for i in l2]
	
def f3(In):
	l1 = [i*i for i in In]
	l2 = sorted(l1)
	return [i*i for i in l1 if i<(0.5*0.5)]
	
In = [random.random() for i in range(100000)]

cProfile.run('f1(In)')
cProfile.run('f2(In)')
cProfile.run('f3(In)')