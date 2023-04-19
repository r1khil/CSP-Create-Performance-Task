#import statements
import turtle

import random

#create window------------------------------------------------
wn = turtle.Screen()


#starting variables --------------------------------

lifes = 3

points = 0

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
  

# check the answer

def check_answer():
  global correct_answer
  if answer == random_flag:
    print("Correct!")
    correct_answer = True
  else:
    print("Incorrect!")
    correct_answer = False
  
# update score


def update_score():
  global points 
  global lifes
  if correct_answer == True:
    points = points + 1
    print("Points", str(points))
    print("Lifes", str(lifes))
  if correct_answer == False:
    lifes = lifes - 1
    print("Points", str(points))
    print("Lifes", str(lifes))


    

# wrap everything in a run

def run():
  choose_flag()
  display_flag()
  question()
  check_answer()
  update_score()

# running program

while lifes > 0:
  run()
  if lifes == 0:
    again = str(input("Do you want to play again? (y/n): "))
    if again == "y":
        lifes = 3
        continue
    else:
        exit()




wn.mainloop()