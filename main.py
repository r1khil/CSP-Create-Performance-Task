import turtle

import random

import os
wn = turtle.Screen()


lifes = 4

points = 1

turtle.register_shape('canada.gif')

turtle.register_shape('brazil.gif')

turtle.register_shape('china.gif')

turtle.register_shape('germany.gif')

turtle.register_shape('ireland.gif')

turtle.register_shape('italy.gif')

turtle.register_shape('japan.gif')

turtle.register_shape('sweden.gif')

turtle.register_shape('mexico.gif')

flag = ["canada.gif", 'brazil.gif', 'mexico.gif', 'china.gif', 'german.gif', 'ireland.gif', 'italy.gif', 'japan.gif', 'sweden.gif',]


def run():
  global flag_chosen
  flag_chosen = random.choice(flag)
  
  global aespa
  aespa = turtle.Turtle()

  aespa.shape(flag_chosen)
  
  global answer
  answer = input("What flag is this? ")

while True:

  print("A flag will pop up on the screen. Enter the country name of the flag. Add a .gif to the end of your answer and use all lowercase. For example, japan should be written as japan.gif. The United States should be written as usa.gif ")

  run()

  while lifes > 0:
    if answer == flag_chosen:
      print("slay")
      points = points + 1
      print("Points:", str(points))
      print("Lifes:", str(lifes))
      turtle.clearscreen()
      run()
    else:
      lifes = lifes - 1
      print("Points:", str(points))
      print("Lifes:", str(lifes))
      turtle.clearscreen()
      run()
    if points == 9:
      print("You win!")
      exit()


  wn.mainloop()