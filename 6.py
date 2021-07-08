def calc():
    a = 3
    b = 5
    def mul_add(x):
        return a * x + b    
    return mul_add(1)        
 
c = calc()
print(dir(c))

