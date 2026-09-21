# File: logistic_gui.py
# A program to graph the logistic function using GUI input fields.

from graphics import *


def main():
    win = GraphWin("Logistic Function GUI", 700, 450)

    # Labels and entry boxes.
    start_label = Text(Point(120, 30), "Starting value:")
    start_entry = Entry(Point(230, 30), 10)

    iterations_label = Text(Point(390, 30), "Iterations:")
    iterations_entry = Entry(Point(500, 30), 10)

    start_label.draw(win)
    start_entry.draw(win)
    iterations_label.draw(win)
    iterations_entry.draw(win)

    # Draw button.
    button = Rectangle(Point(570, 15), Point(650, 45))
    button_text = Text(Point(610, 30), "Graph")

    button.draw(win)
    button_text.draw(win)

    # Draw axes.
    x_axis = Line(Point(50, 400), Point(650, 400))
    y_axis = Line(Point(50, 70), Point(50, 400))

    x_axis.draw(win)
    y_axis.draw(win)

    # Wait for the user to click the Graph button.
    win.getMouse()

    x = float(start_entry.getText())
    iterations = int(iterations_entry.getText())

    previous_point = None

    for i in range(iterations):
        x = 3.9 * x * (1 - x)

        graph_x = 50 + (i + 1) * (550 / iterations)
        graph_y = 400 - x * 300

        current_point = Point(graph_x, graph_y)
        current_point.draw(win)

        if previous_point is not None:
            line = Line(previous_point, current_point)
            line.draw(win)

        previous_point = current_point

    # Change the button text to Exit.
    button_text.setText("Exit")

    # Wait for one more click, then close.
    win.getMouse()
    win.close()


main()