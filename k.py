import math

def count_digits(n):
    if n == 0:
        return 1
    n = abs(n)
    return math.floor(math.log10(n)) + 1

        
def karat(x, y):
        n = count_digits(x if x > y else y) # number of digits
        base = 10 # base 10
        a = x // (10 ** (n // 2)) 
        b = x % (10 ** (n // 2))
        c = y // (10 ** (n // 2))
        d = y % (10 ** (n // 2))
        
        print(f'n: {n}\nbase: {base}\na: {a}\nb: {b}\nc: {c}\nd: {d}\n')
        
        #step 1: e = a*c
        e = a*c
        #step 2: f = b*d
        f = b*d
        #step 3: g = (a+b)*(c+d) 
        g = (a+b)*(c+d)
        #4: h = g-e-f
        h = g-e-f
        #5: (10^4) *e + (10^2) * h + f 
        return (base**n) * e + (base**2) * h + f
       

print(4321 // 100) #100 is 10^2
print(count_digits(4321))

print(karat(1234, 5678)) #expected: 7006652


#karat(3141592653589793238462643383279502884197169399375105820974944592, 2718281828459045235360287471352662497757247093699959574966967627)