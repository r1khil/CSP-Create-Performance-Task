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

def p_update(points):
  points = points + 1
  return points

def l_update(lifes):
  lifes = lifes - 1
  return lifes

def check_answer():
  global correct_answer
  if answer == random_flag:
    print("Correct!")
    print(p_update(current_points))
  else:
    print("Incorrect!")
    print(l_update(current_lifes))

    

# wrap everything in a run

def run():
  choose_flag()
  display_flag()
  question()
  check_answer()

# running program

while current_lifes > 0:
  run()
  if current_lifes == 0:
    again = str(input("Do you want to play again? (y/n): "))
    if again == "y":
        current_lifes = 3
        continue
    else:
        exit()



wn.mainloop()