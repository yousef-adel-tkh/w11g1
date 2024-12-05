def isLeap(y): 
    leap = False
    if y % 4 == 0:
        if y % 100 == 0:
            if y % 400 == 0: 
                leap = True
        else: 
            leap = True
    return leap

def pointInTriangle(b,h,x,y):
    
    ret = 1 # outside
    if b <= 0 or h <= 0:
        ret = -1
    else:
        if (0 <= x <= b and  0 <= y <= h):
            m = (0 - h) / (b - 0)
            c = h 
            yTri = m*x + c
            if y == yTri: 
                ret = 2 # on
            elif y < yTri:
                ret = 0 # inside

    return ret


#     return ret

def gradeClassification(grade):
    if (grade <= 100) and (grade >= 0):
        if grade >= 70:   
            return 0
        elif grade >= 40: 
            return 1
        else:             
            return 2
    else: 
        return -1
    
def isPrime(n):

    if not isinstance(n, int):
        raise TypeError('cannot check primality of non-integer')

    def inner(n, d=2):
        if n <= 1: 
            return False
        if d < n:
            if n % d == 0:
                return False
            return inner(n, d+1)
        return True
    
    return inner(n)
        
def getInvestmentValue(investmentAmount, annualRate, years):

    if investmentAmount <= 0 or annualRate <= 0 or years <= 0:
        raise ValueError("all inputs must be positive integers")

    monthlyRate = ( annualRate / 12 ) / 100
    months = years * 12
    return round( investmentAmount * ( 1 + monthlyRate ) ** months, 2)

print(getInvestmentValue(1,12,1))

