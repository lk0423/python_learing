import turtle

colors = ['red', 'purple', 'blue', 'green', 'yellow', 'orange']
t = turtle.Pen()
sides = 6
turtle.bgcolor('black')
for x in range(360):
    t.pencolor(colors[x % sides])
    t.forward(x * 3 / sides + x)
    t.left(360 / sides + 1)
    t.width(x * sides / 200)
