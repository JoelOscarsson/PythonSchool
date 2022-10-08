from geometry import shape

class Circle(shape):
    def __init__(self, x_pos, y_pos, r):
        super().__init__(x_pos, y_pos)
        self.radius = r

    def area(self):
        return self.radius**2*3.14

    def omkrets(self):
        return 2*self.radius*3.14
