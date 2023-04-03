import turtle

import random

import os
wn = turtle.Screen()


lifes = 3

points = 0

turtle.register_shape('canada.gif')

turtle.register_shape('usa.gif')

turtle.register_shape('mexico.gif')

flag = ["canada.gif", 'usa.gif', 'mexico.gif']


def run():
  global flag_chosen
  flag_chosen = random.choice(flag)
  
  global aespa
  aespa = turtle.Turtle()

  aespa.shape(flag_chosen)
  
  global answer
  answer = input("What flag is this? ")

print("A flag will pop up on the screen. Enter the country name of the flag. Add a .gif to the end of your answer and use all lowercase. For example, japan should be written as japan.gif. The United States should be written as usa.gif ")

run()

while lifes > 0:
  if answer == flag_chosen:
    print("slay")
    points = points + 1
    print(points)
    print(lifes)
    turtle.clearscreen()
    run()
  else:
    lifes = lifes -1
    print(points)
    print(lifes)
    turtle.clearscreen()
    run()

if lifes == 0:
  print("Sorry, you lost.")  
  play_again = input("Would you like to play again? (Y/N) ")
  if play_again == "Y":
    os.execl(sys.executable, sys.executable, *sys.argv)
  if play_again == "N":
    exit()

wn.mainloop()