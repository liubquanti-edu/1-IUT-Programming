class Rectangle:
	def __init__(self, x, y, largeur, hauteur):
		self.x = x
		self.y = y
		self.largeur = largeur
		self.hauteur = hauteur

	def surface(self):
		return self.largeur * self.hauteur

	def deplacerX(self, dx):
		return Rectangle(self.x + dx, self.y, self.largeur, self.hauteur)

	def __eq__(self, other):
		if not isinstance(other, Rectangle):
			return False
		return (self.x == other.x and self.y == other.y and
				self.largeur == other.largeur and self.hauteur == other.hauteur)

	def __lt__(self, other):
		if not isinstance(other, Rectangle):
			return NotImplemented
		return self.surface() < other.surface()
