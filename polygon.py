# File: polygon.py
# A program to draw a regular polygon using a given number of sides and radius.

from graphics import *
import math


def main():
    sides = int(input("Enter the number of sides: "))
    radius = float(input("Enter the radius: "))

    win = GraphWin("Regular Polygon", 500, 500)

    center_x = 250
    center_y = 250
    angle = 360 / sides

    vertices = []

    for i in range(sides):
        degrees = i * angle
        radians = math.radians(degrees)

        x = center_x + radius * math.cos(radians)
        y = center_y + radius * math.sin(radians)

        vertices.append(Point(x, y))

    polygon = Polygon(vertices)
    polygon.draw(win)

    win.getMouse()
    win.close()


main()