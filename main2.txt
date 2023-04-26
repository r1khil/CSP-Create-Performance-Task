#import statements
import turtle

import random

#create window------------------------------------------------
wn = turtle.Screen()


#starting variables --------------------------------

current_points = 0

current_lifes = 3

playing = True



#registering images ------------------------------------------------


turtle.register_shape('canada.gif')

turtle.register_shape('brazil.gif')

turtle.register_shape('china.gif')

turtle.register_shape('germany.gif')

turtle.register_shape('ireland.gif')

turtle.register_shape('italy.gif')

turtle.register_shape('japan.gif')

turtle.register_shape('sweden.gif')

turtle.register_shape('mexico.gif')


#creating list of flags ------------------------------------------------

flag = ["canada.gif", 'brazil.gif', 'mexico.gif', 'china.gif', 'germany.gif', 'ireland.gif', 'italy.gif', 'japan.gif', 'sweden.gif']

#creating turtle ------------------------------------------------

screen = turtle.Turtle()

#functions ------------------------------------------------------------------

# select the flag

def choose_flag():
  global random_flag
  random_flag = random.choice(flag)

# display flag and ask questions

def display_flag():
  screen.shape(random_flag)
  
def question():
  global answer
  answer = input("What flag is this? ")
  answer += ".gif"
  

# check the answer and update score

def add_points(pts, lfs):
  pts = pts + 1
  print("Current points:", pts)
  print("Current lifes:", lfs)
  return pts

def remove_life(lfs, pts):
  lfs = lfs - 1
  print("Current points:", pts)
  print("Current lifes:", lfs)
  return lfs
 
 

# running program

while current_lifes > 0:
  choose_flag()
  display_flag()
  question()

  if answer == random_flag:
    current_points = add_points(current_points, current_lifes)
  else:
    current_lifes = remove_life(current_lifes, current_points)

  if current_lifes == 0:
    again = str(input("You lost! Do you want to play again? (y/n): "))
    if again == "y":
        current_points = 0
        current_lifes = 3
        print("Points have been reset. Current points:", current_points)
        print("Lifes have been reset. Current lifes:", current_lifes)
    else:
        exit()



wn.mainloop()