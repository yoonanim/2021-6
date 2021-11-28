import turtle as t

def penup():
    t.up()

def pendown():
    t.down()


def black_color():
    t.color("black")

def white_color():
    t.color("white")

def red_color():
    t.color("red")

def yellow_color():
    t.color("yellow")

def green_color():
    t.color("green")

def purple_color():
    t.color("purple")

def begin_fill():
    t.begin_fill()

def end_fill():
    t.end_fill()

def draw_ondrag(x, y):
    t.ondrag(None)
    t.goto(x, y)
    t.ondrag(draw_ondrag)

def pensize_1():
    t.pensize(1)
def pensize_3():
    t.pensize(3)
def pensize_5():
    t.pensize(5)
def pensize_0():
    t.pensize(100)

def bgcolor_white():
    t.bgcolor("white")
def bgcolor_grey():
    t.bgcolor("grey")
def bgcolor_black():
    t.bgcolor("black")

screen = t.Screen()
screen.setup(1000, 650)
screen.bgpic("pic.png")
screen.update()

def interface_remove() :
    screen.bgpic("nopic")
    screen.update()

def interface_reupdate() :
    screen.bgpic("pic.png")
    screen.update()

t.bgcolor("grey")
t.pensize(3)

t.onscreenclick(draw_ondrag)
t.onkeypress(black_color, "b")
t.onkeypress(white_color, "w")
t.onkeypress(red_color, "r")
t.onkeypress(yellow_color, "y")
t.onkeypress(green_color, "g")
t.onkeypress(purple_color, "p")
t.onkeypress(penup, "Up")
t.onkeypress(pendown, "Down")
t.onkeypress(begin_fill, "f")
t.onkeypress(end_fill, "e")
t.onkeypress(pensize_1, "1")
t.onkeypress(pensize_3, "2")
t.onkeypress(pensize_5, "3")
t.onkeypress(pensize_0, "0")
t.onkeypress(bgcolor_white, "7")
t.onkeypress(bgcolor_grey, "8")
t.onkeypress(bgcolor_black, "9")
t.onkeypress(interface_remove, "m")
t.onkeypress(interface_reupdate, "i")
t.listen()
