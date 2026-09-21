# File: logistic_lines.py
# A program to graph the logistic function and connect adjacent points.

from graphics import *


def main():
    x = float(input("Enter a starting value between 0 and 1: "))

    win = GraphWin("Logistic Function with Lines", 600, 400)

    # Draw axes.
    x_axis = Line(Point(50, 350), Point(550, 350))
    y_axis = Line(Point(50, 50), Point(50, 350))

    x_axis.draw(win)
    y_axis.draw(win)

    previous_point = None

    for i in range(10):
        x = 3.9 * x * (1 - x)

        graph_x = 50 + (i + 1) * 45
        graph_y = 350 - x * 300

        current_point = Point(graph_x, graph_y)
        current_point.draw(win)

        if previous_point is not None:
            line = Line(previous_point, current_point)
            line.draw(win)

        previous_point = current_point

    win.getMouse()
    win.close()


main()