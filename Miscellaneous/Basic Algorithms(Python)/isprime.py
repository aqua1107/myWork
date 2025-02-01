import math
def isprime(x):
    for i in range(2, math.ceil(x**(1/2)+1)):
        if x % i == 0:
            return False
        else:
            return True

    