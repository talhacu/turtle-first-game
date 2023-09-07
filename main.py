import turtle

turtle.setup(500, 500)
screen = turtle.Screen()
screen.bgcolor("light blue")
screen.title("Çizme Oyunu")



isaret =turtle.Turtle()
isaret.shape("turtle")
turtle.showturtle()

def ileri():
    isaret.forward(45)


def sola():
    isaret.left(45)

def saga():
    isaret.right(45)

def geri():
    isaret.back(45)


screen.onkey(ileri, "Up")
screen.onkey(sola, "Left")
screen.onkey(saga, "Right")
screen.onkey(geri, "Down")

screen.listen()
turtle.mainloop()
