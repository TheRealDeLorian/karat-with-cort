import math

def karat(x, y):
        if x < 10 and y < 10:
                return x*y
        
        # print(f'x: {x}\ny: {y}\n')
        n = len(str(x if x > y else y)) # number of digits
        base = 10 # base 10
        m = math.ceil(n / 2)
        # print(f'n: {n}\nm: {m}')
        a = x // (base ** m) 
        b = x % (base ** m)
        c = y // (base ** m)
        d = y % (base ** m)
        
        # print(f'm: {m}\nn: {n}\nbase: {base}\na: {a}\nb: {b}\nc: {c}\nd: {d}\n')
        
        #step 1: e = a*c
        e = karat(a,c)
        #step 2: f = b*d
        f = karat(b,d)
        #step 3: g = (a+b)*(c+d) 
        g = karat(a+b, c+d)
        #step 4: h = g-e-f
        h = g-e-f
        # print(f'e: {e}\nf: {f}\ng: {g}\nh: {h}\n')
        #step 5: (10^4) *e + (10^2) * h + f 
        # print(f"e: {e}, h: {h} ")
        basepowm = (base**m)

        # bigNum = (base**m)**2
        # bigNumWithoutBase = bigNum / base
        # for x in range (bigNumWithoutBase):
        #         e = (e<<3) + (e<<1) #multiplies by 10 once.
                
        for x in range (m):
                h = (h<<3) + (h<<1) #multiplies by 10 once.
        
        # return (e*(base**m)**2)  + (h*(base**m)) + f
        return ((e*(base**m)**2) + h) + f
        # i = karat(e, basepowm**2) + karat(h, basepowm)
        # return (i + f)
       


print(karat(1234, 5678)) #expected: 7006652
print(karat(12345, 6789)) # 83810205
print(karat(123456, 789123)) # 97421969088
print(karat(12345678910, 10987654321)) # 1.3565005e+20

print(karat(3141592653589793238462643383279502884197169399375105820974944592, 2718281828459045235360287471352662497757247093699959574966967627))