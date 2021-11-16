class fraction:
    def __init__(self,N,D):
        self.N=N
        self.D=D

    def __add__(self,other):
        if self.D == other.D:
            return('\n'+str(self.N + other.N)+'\n____\n'+str(self.D))
        else:
            a=self.N * other.D
            b=self.D * other.N
            c=self.D * other.D
            return ('\n'+str(a+b)+'\n____\n'+str(c))

    def __sub__(self, other):
        if self.D == other.D:
            return ('\n'+str(self.N - other.N) + '\n____\n' + str(self.D))
        else:
            a = self.N * other.D
            b = self.D * other.N
            c = self.D * other.D
            return ('\n'+str(a+b)-'\n____\n'+str(c))

    def __mul__(self, other):
        return('\n'+str(self.N * other.N)+'\n____\n'+str(self.D * other.D))

    def __truediv__(self, other):
        return ('\n'+str(self.N * other.D) + '\n____\n' + str(self.D * other.N))


    def show(self):
        print('\n'+str(self.N)+'______\n'+str(self.D))


print('enter the friction1 :')
n1=int(input())
d1=int(input())
s1=fraction(n1,d1)
s1.show()
print('enter the friction2 :')
n2=int(input())
d2=int(input())
s2=fraction(n2,d2)
s2.show()
print('choose:\n1.add\n2.sub\n3.mul\n4.divide\n')
c = int(input())
if c == 1:
    print(s1+s2)
if c==2:
    print(s1-s2)
if c==3:
    print(s1*s2)
if c==4:
    print(s1/s2)