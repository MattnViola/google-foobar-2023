# Credit to https://math.stackexchange.com/questions/2052179/how-to-find-sum-i-1n-left-lfloor-i-sqrt2-right-rfloor-a001951-a-beatty-s

maxCoeff = 4142135623730950488016887242096980785696718753769480731766797379907324784621070388503875343276415727
def calcCoeff(n):
    return (maxCoeff*n)//(10**100)

def recurse(n):
    if n == 1:
        return 1
    if n < 1:
        return 0
    a = calcCoeff(n)
    return a*n + n*(n+1)//2 - a*(a + 1)//2 - recurse(a)  

def solution(s):
    return str(recurse(int(s)))
    

    
     

print(solution('5'))