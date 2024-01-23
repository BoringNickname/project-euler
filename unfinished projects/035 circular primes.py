#Project Euler Problem 035: Circular Primes
# %%
import numpy
import itertools

def primesfrom2to(n):
    """ Input n>=6, Returns a array of primes, 2 <= p < n """
    sieve = numpy.ones(n//3 + (n%6==2), dtype=numpy.bool)
    for i in range(1,int(n**0.5)//3+1):
        if sieve[i]:
            k=3*i+1|1
            sieve[       k*k//3     ::2*k] = False
            sieve[k*(k-2*(i&1)+4)//3::2*k] = False
    return numpy.r_[2,3,((3*numpy.nonzero(sieve)[0][1:]+1)|1)]

# %%
primes = primesfrom2to(1000000)
# %%
def check_cirucularitty(n):
    n_list = [int(x) for x in list(str(n))]
    n_perms = set(itertools.permutations(n_list))
    n_perms_conv = [int(''.join(map(str,n_list)))]

# %%
n_list = [2,4,3]
n_perms = [int(''.join(map(str, x))) for x in list(set(itertools.permutations(n_list)))]
n_perms
# %%
sd = (1,2,3)
type(sd)
res = int(''.join(map(str, sd)))
res
# %%
def first_primality_check(lst):
    if lst[-1]==2 or lst[-1]==5 or lst[-1]==4 or lst[-1] == 6 or lst[-1] == 8 or lst[-1] == 0:
        return False
    else:
        return True

def second_primality_check(rot_list):
    for number in perm_list:
        if int(''.join(map(str, number))) not in primes:
            return False

primes1to100 = primesfrom2to(100)
refined = []
for prime in primes1to100:
    if first_primality_check([int(x) for x in list(str(n))]):
        pass
    else:
        primes1to100 = primes1to100[primes1to100!=prime]


print('yeehaw', primes1to100)

# %%
res = (2,3,2)
res = int(''.join(map(str, res)))
res
# %%
# %%
