import math
def fact(n):
    if n<=0:
        raise ValueError("please define a number starting from 1")
    res=1
    for i in range(1,n+1):
        res*=i
    return res

def prime(n):
    if n<=0:
        raise ValueError("please define a number starting from 2")
    if n==1:
        return False
    for i in range(2,int(math.sqrt(n)+1)):
        if n%i == 0:
            return False
    return True

def area(n):
    if n<=0:
        raise ValueError("please define a number starting from 1")
    return math.pi*n**2