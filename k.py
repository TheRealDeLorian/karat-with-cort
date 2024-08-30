import math

def karat(x, y):
        if x < 10 and y < 10:
                return x*y
        
        print(f'x: {x}\ny: {y}\n')
        n = len(str(x if x > y else y)) # number of digits
        base = 10 # base 10
        m = math.ceil(n / 2)
        # print(f'n: {n}\nm: {m}')
        a = x // (10 ** m) 
        b = x % (10 ** m)
        c = y // (10 ** m)
        d = y % (10 ** m)
        
        print(f'm: {m}\nn: {n}\nbase: {base}\na: {a}\nb: {b}\nc: {c}\nd: {d}\n')
        
        #step 1: e = a*c
        e = a*c
        #step 2: f = b*d
        f = b*d
        #step 3: g = (a+b)*(c+d) 
        g = (a+b)*(c+d)
        #4: h = g-e-f
        h = g-e-f
        print(f'e: {e}\nf: {f}\ng: {g}\nh: {h}\n')
        #5: (10^4) *e + (10^2) * h + f 
        # print(f'e: {e}')
        # print(base**n)
        # print(h)
        # print(base**m)
        # print(f)
        return (e*(base**m)**2)  + (h*(base**m)) + f
       

print(4321 // 100) #100 is 10^2

print(karat(1234, 5678)) #expected: 7006652
print(karat(12345, 6789)) # 83810205
print(karat(123456, 789123)) # 97421969088
print(karat(12345678910, 10987654321)) # 1.3565005e+20

print(karat(3141592653589793238462643383279502884197169399375105820974944592, 2718281828459045235360287471352662497757247093699959574966967627))