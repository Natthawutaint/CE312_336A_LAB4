#EX 1

class Cylinder():
    def __init__(self, radius, height):
        self.r = radius
        self.h = height

    def calculate(self):
        self.cal = 3.14 * (self.r*self.r) * self.h
        return self.cal

Cylinder1 = Cylinder(5, 10)
print("1st Cylinder = " + ('{:.2f}'.format(Cylinder1.calculate())))

Cylinder2 = Cylinder(7, 13)
print("2nd Cylinder = " + ('{:.2f}'.format(Cylinder2.calculate())))