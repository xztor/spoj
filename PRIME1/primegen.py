import operator
import itertools

def isqrt(n):
 x = n
 y = (x + 1) // 2
 while y < x:
  x = y
  y = (x + n // x) // 2
 return x

def static_vars(**kwargs):
    def decorate(func):
        for k in kwargs:
            setattr(func, k, kwargs[k])
        return func
    return decorate

@static_vars(m_known=10, primes_known=set([2,3,5,7]))
def primes_until(m):
 if m == primes_until.m_known:
   return primes_until.primes_known
 elif m < primes_until.m_known:
   return set(x for x in primes_until.primes_known if x <= m)
 else:
  p = reduce(operator.sub,
    (set(range(2*k,m+1,k))
      for k in primes_until(isqrt(m))), set([2]+range(3,m,2)))
  primes_until.m_known=m
  primes_until.primes_known = p
  return p

def isprime(n):
 s = isqrt(n)
 return all(n % p <> 0 for p in primes_until(s))

def checkprime(n, primes_until_sqrt):
 return (n > 1) and all(n % p <> 0 or n == p for p in primes_until_sqrt)


import sys
sys.stdin.readline()

first = True
for line in sys.stdin:
 v = line.split()
 m = int(v[0])
 n = int(v[1])
 p = primes_until(isqrt(n))
 if not first:
  print ""
 else:
  first = False
 for i in xrange(m,n+1):
  if checkprime(i,p):
   print i
