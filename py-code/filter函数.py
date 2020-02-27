#def f(x):
#    return x%2==1
#print filter(f,[1,2,3,4,5,6,7,8,9])
from math import sqrt
def f(x):
    return sqrt(x)%2==1 or sqrt(x)%2==0
print filter(f,range(1,101))
