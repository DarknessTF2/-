"""Optional Turtle bonus.

Run this file separately if you want to show a simple drawn logo:
python logo_turtle.py
"""

import turtle


def draw_logo():
    screen = turtle.Screen()
    screen.title("Логотип портфолио")
    screen.bgcolor("white")

    pen = turtle.Turtle()
    pen.speed(4)
    pen.pensize(3)

    # TODO: замени инициалы на свои, если хочешь персональный логотип.
    initials = "IT"

    pen.color("#1f6fbf")
    for _ in range(4):
        pen.forward(120)
        pen.right(90)

    pen.penup()
    pen.goto(60, -75)
    pen.pendown()
    pen.color("#222222")
    pen.write(initials, align="center", font=("Arial", 32, "bold"))

    pen.hideturtle()
    screen.mainloop()


if __name__ == "__main__":
    draw_logo()
