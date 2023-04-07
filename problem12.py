from math import sqrt

count=1
app = 0
n = int(input('n : '))

def num_factors(num):
    factors = 0
    sqrt_num = int(sqrt(num))
    for i in range(1, sqrt_num+1):
        if num % i == 0:
            factors += 2
    if sqrt_num**2 == num:
        factors -= 1
    return factors

while num_factors(app) < n:
    app += count
    count+=1
    if num_factors(app)==n-1:
        print(app)
        break
