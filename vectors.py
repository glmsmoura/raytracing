class Vector:
    """ Manipulating 3D vectors"""

    def __init__(self, x=0.0, y=0.0, z=0.0): #Set Vector with values, 0 is the default
        self.x = float(x)
        self.y = float(y)
        self.z = float(z)

    def __str__(self): #Set an easy way to see vector with string
        return f"({self.x},{self.y},{self.z})"

    def inner_product(self, other): #Define inner product for vectors
        return self.x * other.x + self.y * other.y + self.z * other.z

    def module(self): #Define module operation for vectors
        return self.inner_product(self)**0.5

    def normed(self): #Define normatize operation for vectors
        return self / self.module()

    def __mul__(self, other):
        return Vector(self.x * other, self.y * other, self.z * other)

    def __rmul__(self, other):
        return self.__mul__(other)

    def __truediv__(self, other):
        return Vector(self.x / other, self.y / other, self.z / other)

    def __rtruediv__(self, other):
        return self.__truediv__(1 / other)        

    def __add__(self,other):
        return Vector(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self,other):
        return Vector(self.x - other.x, self.y - other.y, self.z - other.z)
