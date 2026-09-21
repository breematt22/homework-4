# File: logistic_graph.py
# A program to graph the logistic function for 10 iterations.

from graphics import *


def main():
    x = float(input("Enter a starting value between 0 and 1: "))

    win = GraphWin("Logistic Function", 600, 400)

    # Draw axes.
    x_axis = Line(Point(50, 350), Point(550, 350))
    y_axis = Line(Point(50, 50), Point(50, 350))

    x_axis.draw(win)
    y_axis.draw(win)

    for i in range(10):
        x = 3.9 * x * (1 - x)

        graph_x = 50 + (i + 1) * 45
        graph_y = 350 - x * 300

        point = Point(graph_x, graph_y)
        point.draw(win)

    win.getMouse()
    win.close()


main()