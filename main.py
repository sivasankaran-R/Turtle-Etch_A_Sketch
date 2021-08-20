from turtle import Turtle , Screen

tim = Turtle()
screen = Screen()



def w_forward():
  tim.forward(30)

def s_backward():
  tim.backward(30)


def a_left():
  tim.left(10)


def d_right():
  tim.right(10)

def reset():
  tim.clear()
  tim.penup()
  tim.home()
  tim.pendown()
  
screen.listen()
screen.onkey(key="w",fun=w_forward)
screen.onkey(key="s",fun=s_backward)
screen.onkey(key="a",fun=a_left)
screen.onkey(key="d",fun=d_right)
screen.onkey(key="c",fun=reset)