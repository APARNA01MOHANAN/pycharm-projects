class fraction:
    def __init__(self,nr,dr):
        self.dr=dr
        self.nr=nr
        if self.dr<0:
            self.nr=self.nr*-1
            self.dr=self.dr*-1
    def display(self):
        print(f'{self.nr}/{self.dr}')
f1=fraction(2,-6)
f1.display()
f2=fraction(-2,-8)
f2.display()