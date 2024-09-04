import math

def raisePower(input, power):
        returnval = input
        for x in range(power):
                returnval = (returnval<<3) + (returnval<<1) #multiplies by 10 once
        return returnval

def karat(x, y):
        if x < 10 and y < 10:
                return x*y
        
        n = len(str(x if x > y else y)) # number of digits
        base = 10 # base 10
        m = math.ceil(n / 2)
        a = x // (base ** m) 
        b = x % (base ** m)
        c = y // (base ** m)
        d = y % (base ** m)
        
        #step 1: e = a*c
        e = karat(a,c)
        #step 2: f = b*d
        f = karat(b,d)
        #step 3: g = (a+b)*(c+d) 
        g = karat(a+b, c+d)
        #step 4: h = g-e-f
        h = g-e-f
        #step 5: (10^4) *e + (10^2) * h + f
        i = raisePower(e, m + m)
        j = raisePower(h, m)
        
        return (i + j) + f
       

def test_first ():
    assert karat(1234, 5678) == 7006652 #Expected: 7006652

def test_second ():
        assert karat(12345, 6789) == 83810205 #Expected: 83810205

def test_third ():
        assert karat(123456, 789123) == 97421969088 #Expected: 97421969088

def test_fourth ():
        assert karat(12345678910, 10987654321) == 135650052221140070110 #Expected: 135650052221140070110
        
        
        
# print(karat(1234, 5678)) #Expected: 7006652
# print(karat(12345, 6789)) #Expected: 83810205
# print(karat(123456, 789123)) #Expected: 97421969088
# print(karat(12345678910, 10987654321)) #Expected: 135650052221140070110
# print(karat(3141592653589793238462643383279502884197169399375105820974944592, 2718281828459045235360287471352662497757247093699959574966967627))
