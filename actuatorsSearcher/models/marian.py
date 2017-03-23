class Triangle(object):
    def __init__(self, angle1, angle2, angle3):
        self.angle1 = angle1
        self.angle2 = angle2
        self.angle3 = angle3

    number_of_sides = 3

    def check_angles(self, angle1, angle2, angle3):
        sum = angle1 + angle2 + angle3
        if sum == 180:
            return True
        else:
            return False


t = Triangle(1, 2, 3)
print(t.number_of_sides)
t.number_of_sides = 4
print(t.number_of_sides)
Triangle.number_of_sides = 5
print(t.number_of_sides)

t2 = Triangle(1, 2, 3)
print(t2.number_of_sides)

my_triangle = Triangle(90, 30, 60)
print(my_triangle.number_of_sides)
print(my_triangle.check_angles())
