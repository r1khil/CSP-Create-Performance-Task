#import statements
import turtle

import random

#create window------------------------------------------------
wn = turtle.Screen()


#starting variables --------------------------------

lifes = 4

points = 1

random_flag = None

answer = None

correct_answer = None

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

flag = ["canada.gif", 'brazil.gif', 'mexico.gif', 'china.gif', 'german.gif', 'ireland.gif', 'italy.gif', 'japan.gif', 'sweden.gif',]

#creating turtle ------------------------------------------------

screen = turtle.Turtle()

#functions ------------------------------------------------------------------

# select the flag

def choose_flag():
  random_flag = random.choice(flag)

# display flag and ask questions

def display_flag():
  screen.shape(random_flag)
  
def question():
  answer = input("What flag is this?")
  

# check the answer

def check_answer():
  if answer == random_flag:
    print("Correct!")
    correct_answer = True
  else:
    print("Incorrect!")
    correct_answer = False
    
# update score

def update_score():
  if correct_answer == True:
    points = points + 1
    print("Points"+ str(points))
    print("Lifes"+ str(lifes))
  if correct_answer == False:
    lifes = lifes - 1
    print("Points"+ str(points))
    print("Lifes"+ str(lifes))


# wrap everything in a run

choose_flag()
print(random_flag)