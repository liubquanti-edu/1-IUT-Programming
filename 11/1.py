class Vecteur:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def __mul__(self, other):
    x = self.x * other.x
    y = self.y * other.y
    return Vecteur(x, y)

def __repr__(self):
    return f"Vecteur(x={self.x}, y={self.y})"

Vecteur.__mul__ = __mul__
Vecteur.__repr__ = __repr__

v1 = Vecteur(2, 3)
v2 = Vecteur(4, 5)
v3 = v1 * v2

repr(v3)