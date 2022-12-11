import turtle


def make_victory_screen():
    turtle.bgcolor("black")
    turtle.penup()
    draw_xmas_star(-300, 100)
    draw_xmas_star(0, 150)
    draw_xmas_star(150, 150)
    turtle.setposition(0, 0)
    turtle.done()


def draw_xmas_star(startX, startY):
    turtle.color('white', 'yellow')
    turtle.penup()
    turtle.setposition(startX, startY)
    turtle.pendown()
    turtle.begin_fill()
    forward = 50
    turtle.forward(forward)
    turtle.left(72)
    turtle.forward(forward)
    for i in range(4):
        turtle.right(144)
        turtle.forward(forward)
        turtle.left(72)
        turtle.forward(forward)
    turtle.end_fill()
    turtle.penup()
