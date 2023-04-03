import turtle

wn = turtle.Screen()


fp = turtle.Turtle()

fp.hideturtle()

fp.speed(0)

def japan():
  #border
  fp.penup()
  fp.goto(-300,150)
  fp.pendown()
  fp.forward(300)
  fp.right(90)
  fp.forward(150)
  fp.right(90)
  fp.forward(300)
  fp.right(90)
  fp.forward(150)
  #inner red
  fp.penup()
  fp.goto(-100,75)
  fp.begin_fill()
  fp.fillcolor("red")
  fp.circle(50)
  fp.end_fill()
  

japan()

wn.mainloop()