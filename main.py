import turtle

#screen settings
turtle.setup(500, 500)
screen = turtle.Screen()
screen.bgcolor("light blue")
screen.title("Çizme Oyunu")

#cursor settings
isaret =turtle.Turtle()
isaret.shape("turtle")
isaret.speed(0)
isaret.pensize(3)
isaret.pencolor("black")
turtle.showturtle()

def ileri():
    isaret.forward(10)
def sola():
    isaret.left(10)
def saga():
    isaret.right(10)
def geri():
    isaret.back(10)

def clear_screen():
    isaret.clear()
def returnHome():
    isaret.penup()
    isaret.home()
    isaret.pendown()


screen.onkey(returnHome, "h")
screen.onkey(ileri, "Up")
screen.onkey(sola, "Left")
screen.onkey(saga, "Right")
screen.onkey(geri, "Down")
screen.onkey(clear_screen, "c")

screen.listen()
turtle.mainloop()
