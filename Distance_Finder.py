import math

x1 = float(input("enter first point x value: "))

y1 = float(input("enter first point y value: "))

x2 = float(input("enter second point x value: "))

y2 = float(input("enter second point y value: "))

point1 = [x1, y1]
point2 = [x2, y2]

print(math.dist(point1, point2))