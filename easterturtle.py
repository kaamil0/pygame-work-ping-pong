import turtle

t = turtle.Turtle()
t.speed(6)
t.pensize(7)

def draw_square():
    t.penup()
    t.goto(-150, 0)
    t.pendown()
    
    t.goto(-50, 0)
    t.goto(-50, 100)
    t.goto(-150, 100)
    t.goto(-150, 0)

def draw_triangle():
    t.penup()
    t.goto(0, 0)
    t.pendown()
    
    t.goto(100, 0)
    t.goto(50, 100)
    t.goto(0, 0)

def draw_L():
    t.penup()
    t.goto(150, 100)
    t.pendown()
    
    t.goto(140, 80)
    t.goto(140, 20)
    t.goto(150, 0)
    t.goto(200, 0)
    t.goto(200, 10)
    t.goto(200, 20)
    t.goto(150, 20)
    t.goto(150, 100)
    t.goto(150, 100)

def draw_rectangle():
    t.penup()
    t.goto(-50, -150)
    t.pendown()
    
    t.goto(50, -150)
    t.goto(50, -100)
    t.goto(-50, -100)
    t.goto(-50, -150)

draw_square()
draw_triangle()
draw_L()
draw_rectangle()

turtle.done()
