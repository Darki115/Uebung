class Vector3():
    def __init__(self, x = 0, y = 0, z = 0):
        self._x = x
        self._y = y
        self._z = z

    def __str__(self):
        return f"({a._x}, {a._y}, {a._z})"
    
    def __add__(self, other):
        return a._x + b._x, a._y + b._y, a._z + b._z
    
    def __sub__(self, other):
        return a._x - b._x, a._y - b._y, a._z - b._z
    
    def multi(self, other):
        return a._x * b._x, a._y * b._y, a._z * b._z
    
    def mult_skal(self, other):
        return a._x * other, a._y * other, a._z * other
    
    def cross(self, other):
        return (a._y * b._z - a._z * b._y), (a._z * b._x - a._x * b._z), (a._x * b._y - a._y * b._x)
    
    def dot(self, other):
        return a._x * b._x + a._y * b._y + a._z * b._z
    
    def normalize(self):
        return ((self._x**2 + self._y**2 + self._z**2)**0.5)
    

a = Vector3(3,4,2)
b = Vector3(2,1,0)

c = a + b
print(c)
d = a - b
print(d)
e = a.multi(b)
print(e)
f = a.mult_skal(2)
print(f)
g = a.cross(b)
print(g)
h = a.dot(b)
print(h)
i = a.normalize()
print(i)