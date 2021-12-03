import turtle, random
border = turtle.Turtle()
border.speed(0)
border.hideturtle()
border.pensize(10)
border.color('green')
border.up()
border.goto(300, 300)
border.down()
border.goto(300, -300)
border.goto(-300, -300)
border.goto(-300, 300)
border.goto(300, 300)

ball = turtle.Turtle()
ball.shape('circle')
ball.up()
randx = random.randint(-290, 290)
randy = random.randint(-290, 290)
ball.goto(randx, randy)

dx = 9
dy = 4
while True:
    x, y = ball.position()
    if x >= 300 or x <=-300:
        dx = -dx
    if y >= 300 or y <=-400:
        dy = -dy
    ball.goto(x + dx, y + dy)
