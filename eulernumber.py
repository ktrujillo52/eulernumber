#Kevin Trujillo 
#Calculate Euler's constant
from decimal import Decimal, getcontext
import time

#Start 
start = time.time()

def f(n, y):
    number = n
    l = range(1, number)  
    count = 0
    coeff = range(1, number)
    k = 1
    for m in coeff:
        k *= m
    for i in l:
        first = 1 / number
        second = i ** first
        const = k * second
        count += Decimal(1) / Decimal(const)
    return Decimal(count) + Decimal(y)
    

#Call function
n = 1
it = 1
getcontext().prec = 100000
y = Decimal()

while (n > 0): 
    function = Decimal(f(n, y))
    #print function
    it += 1
    if n > 10:
        if (Decimal(y) == Decimal(function)):
            end = time.time()
            t = end - start
            #print Decimal(function)
            #print t
            y = Decimal(function)
            with open('numbere.txt', 'w+') as text:
                text.write(str(y))
                text.close()
            it = 0
        else:
            y = Decimal(function)
            #print Decimal(function)
          
    else:
        y = Decimal(function)
        #print Decimal(function)
        
    n = it
    time.sleep(5)


