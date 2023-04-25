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
''''
def p_update():
  points = points + 1
  return points

def l_update():
  lifes = lifes -1 
  return
'''

def check_answer():
  if answer == random_flag:
    adjusted_points = current_points + 1
  if answer != current_points:
    adjusted_lifes = current_lifes - 1
  return adjusted_lifes, adjusted_points

def print_score(adjusted_points, adjusted_lifes):
  print(adjusted_points)
  print(adjusted_lifes)
    
     
    

# wrap everything in a run

def run(adjusted_points, adjusted_lifes):
  choose_flag()
  display_flag()
  question()
  check_answer()
  print_score(adjusted_lifes, adjusted_points)

# running program

while current_lifes > 0:
  run(adjusted_lifes, adjusted_points)
  if current_lifes == 0:
    again = str(input("Do you want to play again? (y/n): "))
    if again == "y":
        current_lifes = 3
        continue
    else:
        exit()



wn.mainloop()