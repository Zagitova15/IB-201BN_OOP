class BoundingRectangle:
    def __init__(self):
        self.x_coords = []
        self.y_coords = []

    def add_point(self, x, y):
        self.x_coords.append(x)
        self.y_coords.append(y)

    def left_x(self):
        return min(self.x_coords)

    def right_x(self):
        return max(self.x_coords)

    def bottom_y(self):
        return min(self.y_coords)

    def top_y(self):
        return max(self.y_coords)

    def width(self):
        return self.right_x() - self.left_x()

    def height(self):
        return self.top_y() - self.bottom_y()

rect = BoundingRectangle()
rect.add_point(-11, -12)
rect.add_point(13, -14)
rect.add_point(-15, 10)
print(rect.left_x(), rect.right_x())
print(rect.bottom_y(), rect.top_y())
print(rect.width(), rect.height())
print()
rect.add_point(-21, -12)
rect.add_point(13, -14)
rect.add_point(-15, 36)
print(rect.width(), rect.height())
print(rect.left_x(), rect.right_x())
print(rect.bottom_y(), rect.top_y())
print()
rect.add_point(-21, 78)
rect.add_point(13, -14)
rect.add_point(-55, 36)
print(rect.bottom_y(), rect.top_y())
print(rect.width(), rect.height())
print(rect.left_x(), rect.right_x())