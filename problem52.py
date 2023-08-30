class Num:
    
    def __init__(self,number) -> None:
        self.digits = set([digit for digit in number])
        #self.digits.sort()
        self.number = number
    
    def multiples(self):
        x = self.digits
        multis = [Num(str(i * int(self.number))) for i in range(2,7)]
        if all(x == num.digits for num in multis):
            return True

n = 1
while True:
    i = Num(str(n))
    if i.multiples():
        print(n)
        break
    n += 1
